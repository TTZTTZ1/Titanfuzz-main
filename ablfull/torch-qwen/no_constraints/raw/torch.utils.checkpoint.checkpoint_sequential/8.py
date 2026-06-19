import torch
from torch.nn import Linear

# Define a simple sequential model
model = torch.nn.Sequential(
    Linear(10, 20),
    Linear(20, 30),
    Linear(30, 40)
)

# Generate input data
input_data = torch.randn(5, 10)

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(model, 2, input_data)