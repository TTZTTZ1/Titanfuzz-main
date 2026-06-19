import torch

# Prepare input data
model = torch.nn.Sequential(torch.nn.Linear(10, 5), torch.nn.ReLU(), torch.nn.Linear(5, 2))
input_tensor = torch.randn(1, 10)
segments = 2
use_reentrant = True

# Call the API
result = torch.utils.checkpoint.checkpoint_sequential(model, segments, input_tensor, use_reentrant=use_reentrant)