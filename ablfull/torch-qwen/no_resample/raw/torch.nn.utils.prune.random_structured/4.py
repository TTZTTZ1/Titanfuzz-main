import torch
from torch.nn.utils import prune

# Create a sample module
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv = torch.nn.Conv2d(1, 1, kernel_size=3)

model = SimpleModel()

# Prepare valid input data
name = 'conv'
amount = 0.5
dim = 1

# Call the API
prune.random_structured(model, name, amount, dim)