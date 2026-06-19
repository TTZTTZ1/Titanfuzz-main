import torch
from torch.nn import Sequential, Linear

# Prepare input data
input_tensor = torch.randn(3, 4)

# Define sequential model
model = Sequential(
    Linear(in_features=4, out_features=5),
    Linear(in_features=5, out_features=6)
)

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(model, 2, input_tensor)