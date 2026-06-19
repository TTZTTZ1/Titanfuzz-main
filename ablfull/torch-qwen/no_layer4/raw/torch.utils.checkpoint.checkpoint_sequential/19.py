import torch
from torch.nn import Sequential, Linear

# Prepare input data
input_tensor = torch.randn(1, 5)

# Define a simple sequential model
model = Sequential(
    Linear(5, 10),
    Linear(10, 15),
    Linear(15, 20)
)

# Parameters for checkpoint_sequential
functions = model
segments = 2
preserve_rng_state = True

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor, preserve_rng_state=preserve_rng_state)