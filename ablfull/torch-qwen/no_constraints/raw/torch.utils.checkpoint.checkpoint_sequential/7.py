import torch
from torch.nn import Linear

def identity(x):
    return x

functions = [Linear(10, 10), Linear(10, 10)]
segments = 2
input_data = torch.randn(5, 10)

result = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_data)