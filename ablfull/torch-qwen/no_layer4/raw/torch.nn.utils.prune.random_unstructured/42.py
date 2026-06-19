import torch
from torch.nn import Module
from torch.nn.utils import prune

# Define a simple model for demonstration purposes
class SimpleModel(Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv = torch.nn.Conv2d(1, 1, kernel_size=3)

model = SimpleModel()

# Prepare valid input data
name = 'conv'
amount = 0.5

# Call the API
prune.random_unstructured(model, name, amount)