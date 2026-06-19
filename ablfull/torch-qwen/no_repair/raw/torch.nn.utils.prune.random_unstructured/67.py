import torch
import torch.nn as nn

class ExampleModule(nn.Module):
    def __init__(self):
        super(ExampleModule, self).__init__()
        self.conv = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3)

module = ExampleModule()
pruned_module = torch.nn.utils.prune.random_unstructured(module.conv, name='weight', amount=0.5)