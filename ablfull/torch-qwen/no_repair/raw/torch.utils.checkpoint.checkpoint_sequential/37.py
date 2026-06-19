import torch
from torch.nn import Sequential, Linear

# Prepare input data
input_tensor = torch.randn(3, 4)

# Define sequential model
model = Sequential(
    Linear(4, 8),
    Linear(8, 16),
    Linear(16, 32)
)

# Call the API
result = torch.utils.checkpoint.checkpoint_sequential(model, 2, input_tensor, use_reentrant=True)