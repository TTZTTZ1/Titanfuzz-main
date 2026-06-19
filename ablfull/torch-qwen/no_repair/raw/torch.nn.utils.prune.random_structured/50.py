import torch
from torch.nn import Module
from torch.nn.utils.prune import random_structured

# Create a dummy model
class DummyModel(Module):
    def __init__(self):
        super(DummyModel, self).__init__()
        self.conv = torch.nn.Conv2d(1, 1, kernel_size=3)

model = DummyModel()

# Prepare input data
name = 'conv.weight'
amount = 0.5
dim = 0

# Call the API
pruned_model = random_structured(model, name, amount, dim)