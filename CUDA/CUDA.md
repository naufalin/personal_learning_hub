# Install CUDA and making sure it works
## Check CUDA version
```bash
>>> nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2021 NVIDIA Corporation
Built on Thu_Nov_18_09:52:33_Pacific_Standard_Time_2021
Cuda compilation tools, release 11.5 V11.5.119
Build cuda_11.5.r11.5/compiler.30672275_0
```
CUDA version is **11.5** according to above

## Install pytorch 
Use link from their [official website](https://pytorch.org/get-started/locally/).
Make sure to use the correct CUDA version, according to the previous step

## Check
Open console to check if it is correctly installed

```python
>>> import torch
>>> torch.cuda.is_available()
True
```


# CUDA Memory
Clear cuda memory

### Option 1
```python
import torch
torch.cuda.empty_cache()
```

### Option 2
```python
import gc
del variables
gc.collect()
```

### Check alloaction of memory in gpu
```python
import torch
print(torch.cuda.memory_summary(device=None, abbreviated=False))
```