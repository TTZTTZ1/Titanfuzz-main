import torch
import torch.nn as nn

class TestModule(nn.Module):
    def __init__(self):
        super(TestModule, self).__init__()
        self.conv = nn.Conv2d(1, 1, kernel_size=3)

module = TestModule()
name = 'conv'
amount = 0.5
torch.nn.utils.prune.random_unstructured(module, name, amount)