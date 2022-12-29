# CGI
This repository contains data and code for the thesis "Contrastive Goal Inference for Dialogue Systems".

This study presents a new contrastive reinforcement learning for multi-domain task-oriented dialogue based on the proposed Contrastive Goal Inference (CGI) where contrastive learning is performed and leveraged without the needs of auxiliary perception loss for data augmentation. The CGI is realized in a reinforcement learning algorithm to learn an informative goal from knowledge-based.

## Requirements
You can directly use docker:
```
sudo docker run -it --rm --shm-size 8G --privileged --gpus all chin0880ee/cgi bash
```
and git clone this repository.

The implementation is based on Python 3.10.4 To install the dependencies used in this project. If you don't use docker, please run:
```
pip install nltk scikit-learn tqdm matplotlib seaborn line-bot-sdk flask torch==1.13.0
```

## Quickstart

### Step 1: Training
For different datasets, please first set up the following parameters in the script `run_train.sh`:
```
data_dir=[xxx]        # directory of the specific dataset
save_dir=[xxx]        # directory to store trained models
```
and then run:
```
bash run_train_[smd or woz].sh
```
Note that more arguments for training can be found in the `main.py`. 

For self-critical sequence training, please set up `num_epochs` larger than `pre_epochs` but no larger than 3 epochs, since self-critical sequence training for a long time might be unstable sometimes.

### Step 2: Testing
For different datasets, please first set up the following parameters in the script `run_test.sh`:
```
data_dir=[xxx]        # directory of the specific dataset
save_dir=[xxx]        # directory of the rrtrained models
output_dir=[xxx]      # directory to store generation results
```
and then run:
```
bash run_test_[smd or woz].sh
```
Note that more arguments for testing can be found in the `main.py`. 

### Step 3: Evaluation
For different datasets, please first set up the following parameters in the script `run_eval.sh`:
```
data_name=[xxx]      # ['smd', 'multiwoz']
data_dir=[xxx]       # directory of the specific dataset
eval_dir=[xxx]       # directory of the generation output
```
and then run:
```
bash run_eval_[smd or woz].sh
```
