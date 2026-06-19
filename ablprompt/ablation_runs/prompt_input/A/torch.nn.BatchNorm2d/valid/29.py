import torch
import torch.nn as nn

# Define a simple model that includes BatchNorm2d
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3)
        self.bn = nn.BatchNorm2d(num_features=64)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        return x

# Create an instance of the model and print its structure
model = SimpleModel()
print(model)