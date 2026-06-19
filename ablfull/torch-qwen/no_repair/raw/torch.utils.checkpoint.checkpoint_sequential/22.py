import torch
from torch.nn import Sequential, Linear

# Prepare input data
input_tensor = torch.randn(1, 10)

# Define a simple sequential model
model = Sequential(
    Linear(10, 5),
    Linear(5, 2)
)

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(model, 2, input_tensor, use_reentrant=True)
print(output)