import torch
import torch.nn as nn

class ExampleModule(nn.Module):
    def __init__(self):
        super(ExampleModule, self).__init__()
        self.conv = nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5)

module = ExampleModule()
name = 'conv'
amount = 0.5

torch.nn.utils.prune.random_unstructured(module, name, amount)