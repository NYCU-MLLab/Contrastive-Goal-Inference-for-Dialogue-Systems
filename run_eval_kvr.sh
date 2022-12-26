#!/bin/bash

# set python path
pythonpath='python3 -m'

# set dir
data_name='kvr'     # ['kvr', 'multiwoz']
data_dir=./data/KVR
eval_dir=./outputs/KVR/state_epoch_8.model

${pythonpath} tools.eval --data_name=${data_name} --data_dir=${data_dir} --eval_dir=${eval_dir}
