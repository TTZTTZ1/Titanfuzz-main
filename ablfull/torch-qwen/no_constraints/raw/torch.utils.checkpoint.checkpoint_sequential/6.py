import torch
from torch.utils.checkpoint import checkpoint_sequential

# Define a simple function to be used in checkpointing
def my_function(x):
    return x * x + 2 * x + 1

# Create a sequential container of functions
functions = [my_function] * 3

# Prepare input data
input_data = torch.randn(5)

# Call the API
output = checkpoint_sequential(functions, segments=2, input=input_data)