import torch
import torch.nn as nn

# Define a simple module for pruning
class SimpleModule(nn.Module):
    def __init__(self):
        super(SimpleModule, self).__init__()
        self.conv = nn.Conv2d(1, 1, kernel_size=3)

module = SimpleModule()
name = 'conv'
amount = 0.5

torch.nn.utils.prune.random_unstructured(module, name=name, amount=amount)