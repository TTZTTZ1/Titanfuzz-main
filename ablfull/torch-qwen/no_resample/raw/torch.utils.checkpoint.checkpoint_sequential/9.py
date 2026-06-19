import torch
from torch.nn import Sequential, Linear

# Prepare input data
input_tensor = torch.randn(1, 10)

# Define sequential model
model = Sequential(
    Linear(10, 20),
    Linear(20, 30),
    Linear(30, 40)
)

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(model, segments=2, input=input_tensor)