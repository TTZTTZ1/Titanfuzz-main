import torch
from torch.nn.utils import prune

# Define a simple module
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv = torch.nn.Conv2d(3, 8, kernel_size=3, padding=1)

model = SimpleModel()

# Prepare valid input data
name = 'conv'
amount = 0.5
dim = 0

# Call the API
prune.random_structured(model, name, amount, dim)