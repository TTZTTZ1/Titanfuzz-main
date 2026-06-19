import torch
import torch.nn as nn

# Task 2: Generate input data
class ExampleModule(nn.Module):
    def __init__(self):
        super(ExampleModule, self).__init__()
        self.conv = nn.Conv2d(in_channels=1, out_channels=1, kernel_size=3)

module = ExampleModule()
name = 'conv'
amount = 0.5

# Task 3: Call the API
torch.nn.utils.prune.random_unstructured(module, name, amount)