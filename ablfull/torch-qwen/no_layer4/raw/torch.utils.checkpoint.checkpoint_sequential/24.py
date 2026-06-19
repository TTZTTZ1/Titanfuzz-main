import torch

# Prepare valid input data
functions = torch.nn.Sequential(torch.nn.Linear(5, 5), torch.nn.ReLU(), torch.nn.Linear(5, 5))
segments = 2
input_data = torch.randn(3, 5)

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_data, use_reentrant=True)