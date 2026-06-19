import torch

# Prepare valid input data
functions = torch.nn.Sequential(torch.nn.Linear(5, 10), torch.nn.ReLU(), torch.nn.Linear(10, 1))
segments = 2
input_tensor = torch.randn(3, 5)

# Call the API
result = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor, use_reentrant=True)