import torch

# Define some sample sequential functions
model = torch.nn.Sequential(
    torch.nn.Linear(10, 5),
    torch.nn.ReLU(),
    torch.nn.Linear(5, 2)
)

# Create an example input tensor
input_tensor = torch.randn(1, 10)

# Call the API with a single segment and use_reentrant set to True
result = torch.utils.checkpoint.checkpoint_sequential(model, 1, input_tensor, use_reentrant=True)