import torch

# Prepare valid input data
sequential_model = torch.nn.Sequential(
    torch.nn.Linear(10, 5),
    torch.nn.ReLU(),
    torch.nn.Linear(5, 1)
)

input_tensor = torch.randn(1, 10)
segments = 2

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(sequential_model, segments, input_tensor, use_reentrant=True)