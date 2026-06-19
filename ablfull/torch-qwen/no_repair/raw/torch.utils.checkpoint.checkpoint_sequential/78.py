import torch
import torch.nn as nn

# Define a simple sequential model
model = nn.Sequential(
    nn.Linear(10, 20),
    nn.ReLU(),
    nn.Linear(20, 10)
)

# Input tensor
input_tensor = torch.randn(5, 10)

# Checkpoint using checkpoint_sequential
output = torch.utils.checkpoint.checkpoint_sequential(model, segments=2, input=input_tensor)