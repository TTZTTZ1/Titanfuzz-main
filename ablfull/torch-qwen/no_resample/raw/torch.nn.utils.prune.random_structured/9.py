import torch
import torch.nn as nn
from torch.nn.utils import prune

# Define a simple module for pruning
class SimpleModule(nn.Module):
    def __init__(self):
        super(SimpleModule, self).__init__()
        self.conv = nn.Conv2d(1, 1, kernel_size=3)

module = SimpleModule()
name = 'conv.weight'
amount = 0.5
dim = 1

prune.random_structured(module, name, amount, dim)