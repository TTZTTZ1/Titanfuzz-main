import torch
from torch.nn import Sequential, Linear

# Define the model as a sequential container of layers
model = Sequential(
    Linear(10, 5),
    Linear(5, 3)
)

# Create input tensor
input_tensor = torch.randn(1, 10)

# Call checkpoint_sequential
output = torch.utils.checkpoint.checkpoint_sequential(model, segments=2, input=input_tensor, use_reentrant=True)