import torch

# Define a simple sequential model
model = torch.nn.Sequential(
    torch.nn.Linear(5, 10),
    torch.nn.ReLU(),
    torch.nn.Linear(10, 5)
)

# Create some dummy input data
input_data = torch.randn(1, 5)

# Call the checkpoint_sequential function
output = torch.utils.checkpoint.checkpoint_sequential(model, segments=2, input=input_data, use_reentrant=False)