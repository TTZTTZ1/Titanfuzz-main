import torch

# Define a simple sequential model
model = torch.nn.Sequential(
    torch.nn.Linear(10, 5),
    torch.nn.ReLU(),
    torch.nn.Linear(5, 2)
)

# Create a dummy input tensor
input_tensor = torch.randn(1, 10)

# Call checkpoint_sequential
output = torch.utils.checkpoint.checkpoint_sequential(model, 2, input_tensor, use_reentrant=True)