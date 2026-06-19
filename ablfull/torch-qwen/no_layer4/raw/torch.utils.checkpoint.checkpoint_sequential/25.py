import torch
from torch.nn import Sequential, Linear

# Prepare input data
functions = Sequential(Linear(10, 5), Linear(5, 2))
segments = 2
input_data = torch.randn(3, 10)

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_data, use_reentrant=True)