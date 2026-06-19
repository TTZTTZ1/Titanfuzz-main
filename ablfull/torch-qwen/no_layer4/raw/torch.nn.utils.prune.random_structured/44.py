import torch
from torch.nn.utils import prune

# Create a sample module
class SampleModule(torch.nn.Module):
    def __init__(self):
        super(SampleModule, self).__init__()
        self.conv = torch.nn.Conv2d(3, 64, kernel_size=3, padding=1)

module = SampleModule()

# Prepare valid input data
name = 'conv.weight'
amount = 0.5
dim = 0

# Call the API
prune.random_structured(module, name, amount, dim)