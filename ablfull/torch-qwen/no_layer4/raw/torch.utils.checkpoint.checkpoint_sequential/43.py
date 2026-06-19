import torch
from torch.nn import Sequential, Linear

# Define some sequential functions
functions = Sequential(Linear(10, 5), Linear(5, 1))

# Input tensor
input_tensor = torch.randn(3, 10)

# Parameters for checkpoint_sequential
segments = 2
preserve_rng_state = True

# Call the API
result = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor, preserve_rng_state=preserve_rng_state)