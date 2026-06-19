import torch

# Define a simple model using Sequential
model = torch.nn.Sequential(
    torch.nn.Linear(10, 5),
    torch.nn.ReLU(),
    torch.nn.Linear(5, 2)
)

# Create a dummy input tensor
input_tensor = torch.randn(1, 10)

# Prepare parameters for checkpoint_sequential
functions = model
segments = 2
use_reentrant = True

# Call the API
result = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor, use_reentrant=use_reentrant)