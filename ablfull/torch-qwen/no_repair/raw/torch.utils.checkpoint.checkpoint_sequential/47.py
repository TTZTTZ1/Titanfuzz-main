import torch
from torch.nn import Sequential, Linear

# Task 2: Generate input data
input_tensor = torch.randn(10, 5)
functions = Sequential(Linear(5, 10), Linear(10, 5))
segments = 2
preserve_rng_state = True

# Task 3: Call the API
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor, preserve_rng_state=preserve_rng_state)