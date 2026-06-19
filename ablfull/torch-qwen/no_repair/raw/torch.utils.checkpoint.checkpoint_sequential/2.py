import torch

# Define a simple sequential model
model = torch.nn.Sequential(
    torch.nn.Linear(10, 5),
    torch.nn.ReLU(),
    torch.nn.Linear(5, 1)
)

# Prepare input data
input_data = torch.randn(1, 10)

# Call the API
result = torch.utils.checkpoint.checkpoint_sequential(model, 2, input_data, use_reentrant=True)