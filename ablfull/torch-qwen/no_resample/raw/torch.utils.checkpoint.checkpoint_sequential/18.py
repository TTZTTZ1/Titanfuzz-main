import torch
from torch.nn import Sequential, Linear

# Prepare input data
input_tensor = torch.randn(1, 10)

# Define sequential functions
sequential_functions = Sequential(
    Linear(10, 5),
    Linear(5, 3)
)

# Call the API
result = torch.utils.checkpoint.checkpoint_sequential(sequential_functions, segments=2, input=input_tensor)