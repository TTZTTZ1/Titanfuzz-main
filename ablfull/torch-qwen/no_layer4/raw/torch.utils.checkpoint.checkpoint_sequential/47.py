import torch
from torch.nn import Sequential, Linear

# Define some dummy functions to be used in checkpointing
def func1(x):
    return x * 2

def func2(x):
    return x + 3

# Create a sequential model or a list of functions
functions = [Linear(10, 5), Linear(5, 1)]
segments = 2

# Prepare the input tensor
input_tensor = torch.randn(10)

# Call the API
result = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor, use_reentrant=True)
print(result)