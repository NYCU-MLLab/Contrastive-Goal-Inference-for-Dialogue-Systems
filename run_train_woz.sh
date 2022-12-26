#!/bin/bash

# set gpu id to use
export CUDA_VISIBLE_DEVICES=0

# set python path according to your actual environment
pythonpath='python3'

# set parameters
seed=13066
data_dir=./data/MULTIWOZ2.1
save_dir=./models/MULTIWOZ2.1_${seed}
num_epochs=10
pre_epochs=10
date
${pythonpath} main.py --data_dir=${data_dir} --save_dir=${save_dir} --num_epochs=${num_epochs} --pre_epochs=${pre_epochs} --seed=${seed} --qr=0.5 --cl=0.5 --kl=0.5 --lr=0.0005
date