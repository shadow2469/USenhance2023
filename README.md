# Prerequisites

\- Python 3

\- CPU or NVIDIA GPU + CUDA CuDNN

# Environment (Using conda)

```
conda install numpy pyyaml mkl mkl-include setuptools cmake cffi typing opencv-python

conda install pytorch torchvision -c pytorch # add cuda90 if CUDA 9

conda install visdom dominate -c conda-forge # install visdom and dominate
```

# Command to run

Please note that root directory is the project root directory.

## Train

```
bash train_cycleGAN.sh
bash train_pix2pix.sh
```

## valid

```
bash valid_cycleGAN.sh
bash valid_pix2pix.sh
```
