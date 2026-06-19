import torch
from torch.nn import Sequential, Linear

# Prepare valid input data
functions = Sequential(Linear(5, 10), Linear(10, 1))
segments = 1
input_tensor = torch.randn(1, 5)

# Call the API
result = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor)