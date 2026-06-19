import torch
import torch.nn as nn
from torch.nn.utils.prune import random_structured

# Define a simple model
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = nn.Linear(5, 1)

model = SimpleModel()

# Prepare valid input data
name = 'linear'
amount = 0.5
dim = 1

# Call the API
pruned_model = random_structured(model, name, amount, dim)