import torch
from torch.nn import Sequential, Linear

# Prepare valid input data
functions = Sequential(Linear(10, 5), Linear(5, 1))
segments = 2
input_tensor = torch.randn(1, 10)

# Call the target API
result = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor, use_reentrant=True)