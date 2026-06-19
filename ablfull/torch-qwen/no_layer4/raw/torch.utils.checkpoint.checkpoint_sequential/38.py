import torch

# Prepare input data
input_tensor = torch.randn(4, 4)

# Define sequential model
sequential_model = torch.nn.Sequential(
    torch.nn.Linear(4, 8),
    torch.nn.ReLU(),
    torch.nn.Linear(8, 4)
)

# Parameters for checkpoint_sequential
functions = sequential_model
segments = 2
preserve_rng_state = True
use_reentrant = False

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor, preserve_rng_state=preserve_rng_state, use_reentrant=use_reentrant)