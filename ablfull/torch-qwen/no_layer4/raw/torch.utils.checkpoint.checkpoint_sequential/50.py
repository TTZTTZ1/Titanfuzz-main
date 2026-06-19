import torch
from torch.nn import Sequential, Linear

# Define some dummy layers
layers = [Linear(5, 5), Linear(5, 5)]
model = Sequential(*layers)

# Prepare input data
input_data = torch.randn(1, 5)

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(model, segments=2, input=input_data, use_reentrant=True)