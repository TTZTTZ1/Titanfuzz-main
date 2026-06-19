import torch
from torch.nn import Sequential, Linear

# Define a simple model as a Sequential container
model = Sequential(Linear(10, 5), Linear(5, 2))

# Prepare input data
input_data = torch.randn(1, 10)

# Call the API with valid parameters
output = torch.utils.checkpoint.checkpoint_sequential(model, segments=2, input=input_data, use_reentrant=True)