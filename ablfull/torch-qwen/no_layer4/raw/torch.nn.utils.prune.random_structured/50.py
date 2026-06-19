import torch
import torch.nn as nn
from torch.nn.utils import prune

# Create a dummy convolutional layer for demonstration
model = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3)

# Prepare valid input data
name = 'weight'
amount = 0.5
dim = 1

# Call the API
prune.random_structured(model, name, amount, dim)