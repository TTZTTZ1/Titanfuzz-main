import torch
from torch import nn

# Define some sample layers
class SimpleLayer(nn.Module):
    def __init__(self):
        super(SimpleLayer, self).__init__()
        self.fc = nn.Linear(10, 10)

    def forward(self, x):
        return self.fc(x)

# Create a sequential model with multiple layers
model = nn.Sequential(
    SimpleLayer(),
    SimpleLayer(),
    SimpleLayer()
)

# Prepare input data
input_data = torch.randn(5, 10)

# Call checkpoint_sequential API
output = torch.utils.checkpoint.checkpoint_sequential(model, segments=2, input=input_data, use_reentrant=True)
print(output.shape)