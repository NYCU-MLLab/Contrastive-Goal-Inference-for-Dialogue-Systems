#!/bin/bash

# set gpu id to use
export CUDA_VISIBLE_DEVICES=0

# set python path according to your actual environment
pythonpath='python3'

# set parameters
seed=$RANDOM
data_dir=./data/MULTIWOZ2.1
save_dir=./models/MULTIWOZ2.1ec01klp_${seed}
num_epochs=10
pre_epochs=10
date
${pythonpath} main.py --data_dir=${data_dir} --save_dir=${save_dir} --num_epochs=${num_epochs} --pre_epochs=${pre_epochs} --seed=${seed}
date