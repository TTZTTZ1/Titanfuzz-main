import torch
from torch.nn import Sequential, Linear

# Prepare input data
input_tensor = torch.randn(1, 3, 224, 224)

# Define sequential model
model = Sequential(
    Linear(3 * 224 * 224, 128),
    Linear(128, 64),
    Linear(64, 10)
)

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(model, segments=2, input=input_tensor, use_reentrant=True)