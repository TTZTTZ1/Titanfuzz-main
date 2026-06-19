import torch
from torch.nn import Sequential, Linear

# Prepare input data
input_tensor = torch.randn(1, 10)

# Define functions
functions = Sequential(
    Linear(10, 5),
    Linear(5, 3)
)

segments = 2

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor, use_reentrant=True)