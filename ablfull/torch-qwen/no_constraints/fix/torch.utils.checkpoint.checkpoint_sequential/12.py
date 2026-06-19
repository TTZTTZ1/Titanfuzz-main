import torch
from torch.utils.checkpoint import checkpoint_sequential

class SimpleModule(torch.nn.Module):

    def __init__(self):
        super(SimpleModule, self).__init__()
        self.fc = torch.nn.Linear(10, 10)

    def forward(self, x):
        return self.fc(x)
modules = [SimpleModule(), SimpleModule()]
input_data = torch.randn(5, 10)
output = checkpoint_sequential(modules, segments=1, input=input_data)