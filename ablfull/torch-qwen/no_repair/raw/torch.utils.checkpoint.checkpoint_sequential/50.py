import torch

# Define a simple model using Sequential
model = torch.nn.Sequential(
    torch.nn.Linear(5, 10),
    torch.nn.ReLU(),
    torch.nn.Linear(10, 1)
)

# Create input tensor
input_tensor = torch.randn(4, 5)

# Call checkpoint_sequential
output = torch.utils.checkpoint.checkpoint_sequential(model, 2, input_tensor, use_reentrant=True)