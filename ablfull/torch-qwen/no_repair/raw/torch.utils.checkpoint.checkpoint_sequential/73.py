import torch

# Define a simple model using torch.nn.Sequential
model = torch.nn.Sequential(
    torch.nn.Linear(10, 20),
    torch.nn.ReLU(),
    torch.nn.Linear(20, 1)
)

# Prepare input tensor
input_tensor = torch.randn(5, 10)

# Call torch.utils.checkpoint.checkpoint_sequential
result = torch.utils.checkpoint.checkpoint_sequential(model, segments=2, input=input_tensor, use_reentrant=True)