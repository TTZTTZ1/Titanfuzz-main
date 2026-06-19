import torch
import torch.nn as nn

# Create a sample module
class SampleModule(nn.Module):
    def __init__(self):
        super(SampleModule, self).__init__()
        self.conv = nn.Conv2d(1, 1, kernel_size=3)

module = SampleModule()
name = 'conv.weight'
amount = 0.5
dim = 1

# Call the API
torch.nn.utils.prune.random_structured(module, name, amount, dim)