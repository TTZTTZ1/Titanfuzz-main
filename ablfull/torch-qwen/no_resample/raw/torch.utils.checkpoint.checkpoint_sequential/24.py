import torch
from torch.nn import Sequential, Linear

# Prepare valid input data
functions = Sequential(Linear(10, 10), Linear(10, 10))
segments = 2
input_tensor = torch.randn(5, 10)

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor)