import torch
from torch.nn import Module

class SimpleModule(Module):
    def __init__(self):
        super(SimpleModule, self).__init__()
        self.conv = torch.nn.Conv2d(1, 6, 5)

module = SimpleModule()
name = 'conv.weight'
amount = 0.5
dim = 1

torch.nn.utils.prune.random_structured(module, name, amount, dim)