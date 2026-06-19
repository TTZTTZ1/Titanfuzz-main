import torch
from torch.nn import Sequential, Linear

# Prepare input data
model = Sequential(Linear(5, 5), Linear(5, 5))
input_data = torch.randn(1, 5)

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(model, segments=2, input=input_data)