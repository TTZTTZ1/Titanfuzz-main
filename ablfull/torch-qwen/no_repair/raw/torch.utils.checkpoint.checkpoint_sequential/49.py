import torch
import torch.nn as nn

# Define some dummy layers
layer1 = nn.Linear(10, 15)
layer2 = nn.ReLU()
layer3 = nn.Linear(15, 20)

# Create a Sequential model
model = nn.Sequential(layer1, layer2, layer3)

# Prepare input data
input_data = torch.randn(5, 10)

# Call checkpoint_sequential
output = torch.utils.checkpoint.checkpoint_sequential(model, segments=2, input=input_data, use_reentrant=True)