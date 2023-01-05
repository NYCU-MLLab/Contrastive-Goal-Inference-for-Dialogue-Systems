#!/bin/bash

# set gpu id to use
export CUDA_VISIBLE_DEVICES=0

# set python path according to your actual environment
pythonpath='python3'

# set parameters
data_dir=./data/MULTIWOZ2.1
save_dir=./models/MULTIWOZ2.1
output_dir=./outputs/MULTIWOZ2.1
ckpt=state_epoch_7.model
beam_size=4
max_dec_len=25

mkdir -p ${output_dir}/${ckpt}

${pythonpath} main.py --test --data_dir=${data_dir} --save_dir=${save_dir} --ckpt=${ckpt} --beam_size=${beam_size} --max_dec_len=${max_dec_len} --output_dir=${output_dir}/${ckpt}
