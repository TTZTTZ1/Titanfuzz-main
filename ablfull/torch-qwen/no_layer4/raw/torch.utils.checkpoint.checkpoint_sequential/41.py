import torch
import torch.nn as nn

# Define a simple model for demonstration purposes
model = nn.Sequential(
    nn.Linear(10, 5),
    nn.ReLU(),
    nn.Linear(5, 1)
)

# Prepare input data
input_data = torch.randn(1, 10)

# Call the checkpoint_sequential function
output = torch.utils.checkpoint.checkpoint_sequential(model, segments=2, input=input_data, use_reentrant=True)
print(output)