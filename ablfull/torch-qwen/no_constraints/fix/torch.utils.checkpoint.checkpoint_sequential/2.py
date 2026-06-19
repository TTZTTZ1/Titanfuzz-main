import torch
from torch.utils.checkpoint import checkpoint_sequential

def func(x):
    return (((x * x) + (2 * x)) + 1)
input_data = torch.randn(5)
output = checkpoint_sequential([func], 1, input_data)