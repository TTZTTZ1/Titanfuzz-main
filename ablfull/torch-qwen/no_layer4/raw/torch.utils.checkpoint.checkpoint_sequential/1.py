import torch
from torch.nn import Sequential, Linear

# Prepare input data
input_tensor = torch.randn(10, 5)

# Define functions
functions = Sequential(
    Linear(5, 10),
    Linear(10, 5)
)

segments = 2

# Call the API
result = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor)