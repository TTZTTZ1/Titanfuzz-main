import torch
from torch.nn.modules.module import Module
from torch.nn.modules.linear import Linear

# Task 2: Generate input data
class MyModule(Module):
    def __init__(self):
        super(MyModule, self).__init__()
        self.fc = Linear(10, 5)

module = MyModule()
name = 'fc.weight'
amount = 0.5
dim = 1

# Task 3: Call the API
torch.nn.utils.prune.random_structured(module, name, amount, dim=dim)