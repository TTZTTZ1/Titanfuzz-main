import torch
import torch.nn as nn
from torch.nn.utils import prune

# Define a simple model for demonstration
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv = nn.Conv2d(1, 6, 5)

model = SimpleModel()

# Prepare input data
name = 'conv'
amount = 0.5
dim = 1

# Call the API
prune.random_structured(model, name, amount=amount, dim=dim)