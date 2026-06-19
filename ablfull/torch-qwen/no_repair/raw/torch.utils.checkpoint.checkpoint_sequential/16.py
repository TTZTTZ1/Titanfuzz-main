import torch
from torch.nn import Sequential, Linear

# Define a simple sequential model
model = Sequential(Linear(5, 10), Linear(10, 1))

# Input tensor
input_tensor = torch.randn(3, 5)

# Parameters for checkpoint_sequential
functions = model
segments = 2
preserve_rng_state = True
use_reentrant = False

# Call the API
result = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor, preserve_rng_state=preserve_rng_state, use_reentrant=use_reentrant)