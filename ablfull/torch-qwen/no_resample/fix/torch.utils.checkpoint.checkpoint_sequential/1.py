import torch
from torch.nn import Sequential, Linear

def my_function(x):
    return (x * 2)
model = Sequential(Linear(10, 5), Linear(5, 1))
input_data = torch.randn(1, 10)
result = torch.utils.checkpoint.checkpoint_sequential([my_function], 1, input_data, use_reentrant=True)