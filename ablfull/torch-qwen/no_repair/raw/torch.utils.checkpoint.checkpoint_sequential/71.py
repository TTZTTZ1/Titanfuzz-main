import torch
import torch.nn as nn

class DummyModule(nn.Module):
    def __init__(self):
        super(DummyModule, self).__init__()
        self.linear = nn.Linear(10, 10)

    def forward(self, x):
        return self.linear(x)

model = DummyModule()
input_data = torch.randn(5, 10)
output = torch.utils.checkpoint.checkpoint_sequential([model], 2, input_data)