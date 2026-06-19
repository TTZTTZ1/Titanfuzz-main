import torch
from torch import nn

# Define a simple sequential model
model = nn.Sequential(
    nn.Linear(10, 5),
    nn.ReLU(),
    nn.Linear(5, 2)
)

# Input tensor
input_tensor = torch.randn(1, 10)

# Parameters for checkpoint_sequential
functions = model
segments = 2
preserve_rng_state = True
use_reentrant = False

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor, preserve_rng_state=preserve_rng_state, use_reentrant=use_reentrant)