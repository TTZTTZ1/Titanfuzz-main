import torch
from torch.nn import Linear

# Define a simple sequential model
model = torch.nn.Sequential(
    Linear(10, 5),
    Linear(5, 3)
)

# Prepare input data
input_data = torch.randn(1, 10)

# Call checkpoint_sequential
output = torch.utils.checkpoint.checkpoint_sequential(model, 1, input_data)