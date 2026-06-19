import torch
from torch.nn import Sequential, Linear

# Prepare valid input data
functions = Sequential(Linear(5, 10), Linear(10, 1))
segments = 2
input_data = torch.randn(3, 5)

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_data, use_reentrant=True)