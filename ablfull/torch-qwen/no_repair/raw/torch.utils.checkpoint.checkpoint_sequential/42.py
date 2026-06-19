import torch
from torch.nn import Sequential, Linear

# Define the functions to be checkpointed
functions = Sequential(
    Linear(5, 5),
    Linear(5, 5)
)

# Input tensor
input_tensor = torch.randn(1, 5)

# Call the checkpoint_sequential function
result = torch.utils.checkpoint.checkpoint_sequential(functions, segments=2, input=input_tensor, use_reentrant=True)
print(result)