import torch
from torch.nn import Sequential, Linear

# Define the functions to be checkpointed
functions = Sequential(
    Linear(10, 5),
    Linear(5, 2)
)

# Prepare the input tensor
input_tensor = torch.randn(1, 10)

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments=2, input=input_tensor, use_reentrant=True)