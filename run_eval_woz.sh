#!/bin/bash

# set python path
pythonpath='python3 -m'

# set dir
data_name='multiwoz'     # ['kvr', 'multiwoz']
data_dir=./data/MULTIWOZ2.1
eval_dir=./outputs/MULTIWOZ2.1/state_epoch_7.model

${pythonpath} tools.eval --data_name=${data_name} --data_dir=${data_dir} --eval_dir=${eval_dir}
