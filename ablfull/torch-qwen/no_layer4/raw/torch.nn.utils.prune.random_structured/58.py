import torch
from torch.nn import Module

class MyModule(Module):
    def __init__(self):
        super(MyModule, self).__init__()
        self.conv = torch.nn.Conv2d(1, 1, kernel_size=3)

module = MyModule()
name = 'conv.weight'
amount = 0.5
dim = 1

torch.nn.utils.prune.random_structured(module, name, amount=amount, dim=dim)