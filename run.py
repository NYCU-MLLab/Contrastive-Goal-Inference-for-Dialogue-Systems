from __future__ import unicode_literals

import os
import json
import logging
import argparse
import torch
import random
import numpy as np

from source.inputter.corpus import KnowledgeCorpus
from source.model.seq2seq import Seq2Seq
from source.utils.engine import Trainer
from source.utils.generator import BeamGenerator
from source.utils.demo import BeamGeneratorDemo
from source.utils.misc import str2bool

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)
line_bot_api = LineBotApi('MLF6o8XFiemEUqqU7S/cewte7/aQ8wCx5usBCxRB28sZA9m9kau5oy5Nkixxiw5bX/08pkV60ry2LfxBWBzj7Fm3mBMkugM7LX3Ik6N0aq2AJWQ7337I3FOaso6leMqwnegcEucmQ46LIDSwqZ08WwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b0065e828ff21b8055e3804bcfbf61f7')

@app.route("/dialog", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

def model_config():
    """
    model_config
    """
    parser = argparse.ArgumentParser()

    # Data
    data_arg = parser.add_argument_group("Data")
    data_arg.add_argument("--data_dir", type=str, default="")
    data_arg.add_argument("--save_dir", type=str, default="./models")
    data_arg.add_argument("--output_dir", type=str, default="./outputs")
    data_arg.add_argument("--embed_file", type=str, default=None)

    # Network
    net_arg = parser.add_argument_group("Network")
    net_arg.add_argument("--embed_size", type=int, default=200)
    net_arg.add_argument("--hidden_size", type=int, default=256)
    net_arg.add_argument("--bidirectional", type=str2bool, default=False)
    net_arg.add_argument("--max_vocab_size", type=int, default=30000)
    net_arg.add_argument("--min_len", type=int, default=1)
    net_arg.add_argument("--max_len", type=int, default=400)
    net_arg.add_argument("--num_layers", type=int, default=1)
    net_arg.add_argument("--max_hop", type=int, default=3)
    net_arg.add_argument("--attn", type=str, default='mlp', choices=['none', 'mlp', 'dot', 'general'])
    net_arg.add_argument("--share_vocab", type=str2bool, default=True)
    net_arg.add_argument("--with_bridge", type=str2bool, default=False)
    net_arg.add_argument("--tie_embedding", type=str2bool, default=True)

    # Training
    train_arg = parser.add_argument_group("Training")
    train_arg.add_argument("--gpu", type=int, default=0)
    train_arg.add_argument("--batch_size", type=int, default=1)
    train_arg.add_argument("--optimizer", type=str, default="Adam")
    train_arg.add_argument("--lr", type=float, default=0.0005)
    train_arg.add_argument("--lr_decay", type=float, default=0.5)
    train_arg.add_argument("--patience", type=int, default=5)
    train_arg.add_argument("--grad_clip", type=float, default=5.0)
    train_arg.add_argument("--dropout", type=float, default=0.2)
    train_arg.add_argument("--num_epochs", type=int, default=10)
    train_arg.add_argument("--pre_epochs", type=int, default=10)
    train_arg.add_argument("--use_embed", type=str2bool, default=True)
    train_arg.add_argument("--log_steps", type=int, default=5)
    train_arg.add_argument("--valid_steps", type=int, default=20)

    # Generation
    gen_arg = parser.add_argument_group("Generation")
    gen_arg.add_argument("--test", action="store_true")
    gen_arg.add_argument("--demo", action="store_true")
    gen_arg.add_argument("--ckpt", type=str, default="best.model")
    gen_arg.add_argument("--beam_size", type=int, default=1)
    gen_arg.add_argument("--max_dec_len", type=int, default=20)
    gen_arg.add_argument("--ignore_unk", type=str2bool, default=True)
    gen_arg.add_argument("--length_average", type=str2bool, default=True)

    config = parser.parse_args()

    return config

@handler.add(MessageEvent, message=TextMessage)
def test_end2end(event):
    global turn_inputs, kb_inputs
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        user_response = event.message.text
        sys_response = demo.forward(turn_inputs=turn_inputs, kb_inputs=kb_inputs, enc_hidden=None, user_response=user_response)
        
        if user_response == "End":
            session_over = True
        else:
            session_over = False

        if session_over==True:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="-------------------------------------"+str(step//2))
            )
            sysinit()
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=sys_response)
            )
            

def sysinit():
    global test_iter, turn_inputs, kb_inputs
    turn_inputs, kb_inputs = demo.generate(data_iter=test_iter, output_dir=config.output_dir, verbos=True)

if __name__ == '__main__':
    seed = 8938
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True
    os.environ['PYTHONHASHSEED'] = str(seed)

    config = model_config()

    config.use_gpu = torch.cuda.is_available() and config.gpu >= 0

    # Data definition
    corpus = KnowledgeCorpus(data_dir=config.data_dir,
                            min_freq=0, max_vocab_size=config.max_vocab_size,
                            min_len=config.min_len, max_len=config.max_len,
                            embed_file=config.embed_file, share_vocab=config.share_vocab)
    corpus.load()

    # Model definition
    model = Seq2Seq(src_field=corpus.SRC, tgt_field=corpus.TGT,
                    kb_field=corpus.KB, embed_size=config.embed_size,
                    hidden_size=config.hidden_size, padding_idx=corpus.padding_idx,
                    num_layers=config.num_layers, bidirectional=config.bidirectional,
                    attn_mode=config.attn, with_bridge=config.with_bridge,
                    tie_embedding=config.tie_embedding, dropout=config.dropout,
                    max_hop=config.max_hop, use_gpu=config.use_gpu)

    # Generator definition
    generator = BeamGenerator(model=model, src_field=corpus.SRC, tgt_field=corpus.TGT, kb_field=corpus.KB,
                            beam_size=config.beam_size, max_length=config.max_dec_len,
                            ignore_unk=config.ignore_unk,
                            length_average=config.length_average, use_gpu=config.use_gpu)
                            
    # demo definition
    demo = BeamGeneratorDemo(model=model, src_field=corpus.SRC, tgt_field=corpus.TGT, kb_field=corpus.KB,
                                beam_size=config.beam_size, max_length=config.max_dec_len,
                                ignore_unk=config.ignore_unk,
                                length_average=config.length_average, use_gpu=config.use_gpu)

    # demo
    if config.demo and config.ckpt:
        test_iter = corpus.create_batches(config.batch_size, data_type="test", shuffle=False)
        model_path = os.path.join(config.save_dir, config.ckpt)
        model.load(model_path)

        turn_inputs, kb_inputs = demo.generate(data_iter=test_iter, output_dir=config.output_dir, verbos=True)          

        app.run(host='0.0.0.0', port=80, debug=True)

