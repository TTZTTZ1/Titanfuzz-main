import torch
from torch.utils.checkpoint import checkpoint_sequential

# Define a simple function to be used in checkpointing
def func(x):
    return x * x + 2 * x + 1

# Prepare input data
input_data = torch.randn(5)

# Call the API
output = checkpoint_sequential([func], 1, input_data)