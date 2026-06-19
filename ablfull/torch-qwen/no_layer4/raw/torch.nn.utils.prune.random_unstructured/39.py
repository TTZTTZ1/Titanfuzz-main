import torch
from torch.nn.utils import prune

# Create a sample module
class SampleModule(torch.nn.Module):
    def __init__(self):
        super(SampleModule, self).__init__()
        self.conv = torch.nn.Conv2d(1, 1, kernel_size=3)

module = SampleModule()

# Prepare input data
name = 'conv.weight'
amount = 0.5

# Call the API
prune.random_unstructured(module, name, amount)