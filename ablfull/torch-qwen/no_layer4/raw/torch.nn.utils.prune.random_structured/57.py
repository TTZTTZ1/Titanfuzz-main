import torch
from torch.nn import Module

class DummyModule(Module):
    def __init__(self):
        super(DummyModule, self).__init__()
        self.conv = torch.nn.Conv2d(1, 1, kernel_size=3)

module = DummyModule()
name = 'conv'
amount = 0.5
dim = 0

torch.nn.utils.prune.random_structured(module, name, amount, dim)