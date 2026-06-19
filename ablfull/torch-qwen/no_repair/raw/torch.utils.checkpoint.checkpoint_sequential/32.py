import torch
from torch.nn import Sequential, Linear

# Define the functions to be checkpointed
functions = Sequential(Linear(10, 5), Linear(5, 2))

# Define the number of segments for checkpointing
segments = 2

# Create random input tensor
input_tensor = torch.randn(4, 10)

# Call the checkpoint_sequential function
result = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor, use_reentrant=True)