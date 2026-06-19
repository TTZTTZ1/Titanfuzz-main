import torch
import torch.nn as nn

class DummyLayer(nn.Module):
    def forward(self, x):
        return x * 2

model = nn.Sequential(
    DummyLayer(),
    DummyLayer()
)

input_data = torch.randn(1, 3, 224, 224)
output = torch.utils.checkpoint.checkpoint_sequential(model, segments=2, input=input_data, use_reentrant=True)