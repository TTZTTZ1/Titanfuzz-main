import torch
from torch.utils.checkpoint import checkpoint_sequential

def my_function(x):
    return (((x * x) + (2 * x)) + 1)
input_data = torch.randn(5)
result = checkpoint_sequential([my_function], 1, input_data)
print(result)