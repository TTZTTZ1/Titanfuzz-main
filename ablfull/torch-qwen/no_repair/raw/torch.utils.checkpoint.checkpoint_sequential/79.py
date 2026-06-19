import torch
from torch.nn import Sequential, Linear

# Prepare valid input data
functions = Sequential(Linear(10, 5), Linear(5, 2))
segments = 2
input_tensor = torch.randn(3, 10)

# Call the API
result = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor, use_reentrant=True)