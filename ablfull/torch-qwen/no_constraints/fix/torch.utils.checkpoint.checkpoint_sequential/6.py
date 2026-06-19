import torch
from torch.utils.checkpoint import checkpoint_sequential

def simple_function(x):
    return (((x * x) + (2 * x)) + 1)
input_data = torch.randn(5)
result = checkpoint_sequential([simple_function], 1, input_data)