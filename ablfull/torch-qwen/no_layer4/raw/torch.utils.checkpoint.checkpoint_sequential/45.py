import torch
from torch.nn import Sequential, Linear

# Prepare input data
input_tensor = torch.randn(1, 5)

# Define sequential model
model = Sequential(
    Linear(5, 10),
    Linear(10, 15)
)

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(model, segments=2, input=input_tensor, use_reentrant=True)