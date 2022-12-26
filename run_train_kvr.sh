#!/bin/bash

# set gpu id to use
export CUDA_VISIBLE_DEVICES=0

# set python path according to your actual environment
pythonpath='python3'

# set parameters
seed=29445
data_dir=./data/KVR
save_dir=./models/KVR_${seed}
num_epochs=10
pre_epochs=10
date
${pythonpath} main.py --data_dir=${data_dir} --save_dir=${save_dir} --num_epochs=${num_epochs} --pre_epochs=${pre_epochs} --seed=${seed} --qr=1 --cl=0.5 --kl=0.1 --lr=0.001
date