#!/bin/bash

# set python path
pythonpath='python3 -m'

# set dir
data_name='kvr'     # ['kvr', 'camrest', 'multiwoz']
data_dir=./data/KVR
eval_dir=./outputs/KVRec01klp_29445_18040/state_epoch_10.model

${pythonpath} tools.eval --data_name=${data_name} --data_dir=${data_dir} --eval_dir=${eval_dir}
