import torch

# Prepare valid input data
functions = torch.nn.Sequential(
    torch.nn.Linear(5, 10),
    torch.nn.ReLU(),
    torch.nn.Linear(10, 2)
)
segments = 2
input_tensor = torch.randn(1, 5)

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor, use_reentrant=True)