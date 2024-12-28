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
Example output:
```
|===========================================================================|
|                  PyTorch CUDA memory summary, device ID 0                 |
|---------------------------------------------------------------------------|
|            CUDA OOMs: 0            |        cudaMalloc retries: 0         |
|===========================================================================|
|        Metric         | Cur Usage  | Peak Usage | Tot Alloc  | Tot Freed  |
|---------------------------------------------------------------------------|
| Allocated memory      |      0 B   |      0 B   |      0 B   |      0 B   |
|       from large pool |      0 B   |      0 B   |      0 B   |      0 B   |
|       from small pool |      0 B   |      0 B   |      0 B   |      0 B   |
|---------------------------------------------------------------------------|
| Active memory         |      0 B   |      0 B   |      0 B   |      0 B   |
|       from large pool |      0 B   |      0 B   |      0 B   |      0 B   |
|       from small pool |      0 B   |      0 B   |      0 B   |      0 B   |
|---------------------------------------------------------------------------|
| Requested memory      |      0 B   |      0 B   |      0 B   |      0 B   |
|       from large pool |      0 B   |      0 B   |      0 B   |      0 B   |
|       from small pool |      0 B   |      0 B   |      0 B   |      0 B   |
|---------------------------------------------------------------------------|
| GPU reserved memory   |      0 B   |      0 B   |      0 B   |      0 B   |
|       from large pool |      0 B   |      0 B   |      0 B   |      0 B   |
|       from small pool |      0 B   |      0 B   |      0 B   |      0 B   |
|---------------------------------------------------------------------------|
| Non-releasable memory |      0 B   |      0 B   |      0 B   |      0 B   |
|       from large pool |      0 B   |      0 B   |      0 B   |      0 B   |
|       from small pool |      0 B   |      0 B   |      0 B   |      0 B   |
|---------------------------------------------------------------------------|
| Allocations           |       0    |       0    |       0    |       0    |
|       from large pool |       0    |       0    |       0    |       0    |
|       from small pool |       0    |       0    |       0    |       0    |
|---------------------------------------------------------------------------|
| Active allocs         |       0    |       0    |       0    |       0    |
|       from large pool |       0    |       0    |       0    |       0    |
|       from small pool |       0    |       0    |       0    |       0    |
|---------------------------------------------------------------------------|
| GPU reserved segments |       0    |       0    |       0    |       0    |
|       from large pool |       0    |       0    |       0    |       0    |
|       from small pool |       0    |       0    |       0    |       0    |
|---------------------------------------------------------------------------|
| Non-releasable allocs |       0    |       0    |       0    |       0    |
|       from large pool |       0    |       0    |       0    |       0    |
|       from small pool |       0    |       0    |       0    |       0    |
|---------------------------------------------------------------------------|
| Oversize allocations  |       0    |       0    |       0    |       0    |
|---------------------------------------------------------------------------|
| Oversize GPU segments |       0    |       0    |       0    |       0    |
|===========================================================================|
```