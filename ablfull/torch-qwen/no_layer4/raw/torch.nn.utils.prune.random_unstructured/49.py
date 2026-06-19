import torch
import torch.nn as nn

# Create a sample module
class SimpleModule(nn.Module):
    def __init__(self):
        super(SimpleModule, self).__init__()
        self.conv = nn.Conv2d(1, 6, 5)

module = SimpleModule()
name = 'conv'
amount = 0.5

# Prune the module
pruned_module = nn.utils.prune.random_unstructured(module, name, amount)