import torch
from torch.nn import Sequential, Linear

# Prepare input data
input_data = torch.randn(10)

# Define a simple sequential model
model = Sequential(Linear(10, 5), Linear(5, 1))

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(model, segments=2, input=input_data)