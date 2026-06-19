import torch
from torch.nn.utils import prune

# Create a simple module
class SimpleModule(torch.nn.Module):
    def __init__(self):
        super(SimpleModule, self).__init__()
        self.linear = torch.nn.Linear(4, 4)

module = SimpleModule()

# Prepare input data
name = 'linear'
amount = 0.5

# Call the API
prune.random_unstructured(module, name, amount)