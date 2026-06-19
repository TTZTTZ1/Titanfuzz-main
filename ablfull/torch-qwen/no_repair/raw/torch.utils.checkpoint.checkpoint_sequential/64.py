import torch
from torch.utils.checkpoint import checkpoint_sequential

# Prepare input data
sequential_model = torch.nn.Sequential(
    torch.nn.Linear(10, 20),
    torch.nn.ReLU(),
    torch.nn.Linear(20, 5)
)
segments = 2
input_tensor = torch.randn(3, 10)

# Call the API
result = checkpoint_sequential(sequential_model, segments, input_tensor, preserve_rng_state=True)