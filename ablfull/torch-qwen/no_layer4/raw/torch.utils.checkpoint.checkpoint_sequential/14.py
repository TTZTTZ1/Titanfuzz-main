import torch

# Prepare input data
functions = torch.nn.Sequential(torch.nn.Linear(5, 5), torch.nn.ReLU(), torch.nn.Linear(5, 5))
segments = 2
input_tensor = torch.randn(1, 5)

# Call the API
result = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor, use_reentrant=True)