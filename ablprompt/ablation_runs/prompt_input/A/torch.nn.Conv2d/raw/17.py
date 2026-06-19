import torch
from torch import nn

# Define a simple model using Conv2d
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv = nn.Conv2d(in_channels=1, out_channels=3, kernel_size=3, stride=1, padding=1)

    def forward(self, x):
        return self.conv(x)

# Create an instance of the model and print its structure
model = SimpleModel()
print(model)