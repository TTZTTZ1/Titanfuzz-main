import torch
from torch.utils.checkpoint import checkpoint_sequential

def my_function(x):
    return (((x * x) + (2 * x)) + 1)
functions = ([my_function] * 3)
input_data = torch.randn(5)