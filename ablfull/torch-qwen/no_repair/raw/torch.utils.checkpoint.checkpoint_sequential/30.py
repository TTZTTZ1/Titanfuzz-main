import torch
from torch.nn import Sequential, Linear

# Define the model as a Sequential container
model = Sequential(
    Linear(10, 20),
    Linear(20, 30),
    Linear(30, 40)
)

# Prepare input data
input_data = torch.randn(5, 10)

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(model, segments=2, input=input_data)