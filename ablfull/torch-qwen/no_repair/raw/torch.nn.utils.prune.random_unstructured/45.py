import torch
import torch.nn as nn

class DummyModel(nn.Module):
    def __init__(self):
        super(DummyModel, self).__init__()
        self.conv = nn.Conv2d(1, 1, kernel_size=3)

model = DummyModel()
name = 'conv'
amount = 0.5
torch.nn.utils.prune.random_unstructured(model, name, amount)