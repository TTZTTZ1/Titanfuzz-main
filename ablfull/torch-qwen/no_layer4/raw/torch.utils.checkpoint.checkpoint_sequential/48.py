import torch
import torch.nn as nn

# Define a simple sequential model
model = nn.Sequential(
    nn.Linear(5, 10),
    nn.ReLU(),
    nn.Linear(10, 1)
)

# Prepare input data
input_data = torch.randn(3, 5)

# Call the checkpoint_sequential function
output = torch.utils.checkpoint.checkpoint_sequential(model, segments=2, input=input_data, use_reentrant=True)