import torch
from torch.nn import Module

class DummyModel(Module):
    def __init__(self):
        super(DummyModel, self).__init__()
        self.conv = torch.nn.Conv2d(1, 1, kernel_size=1)

model = DummyModel()
name = 'conv'
amount = 0.5
torch.nn.utils.prune.random_unstructured(model, name, amount)