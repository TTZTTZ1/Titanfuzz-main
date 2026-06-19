import torch
import torch.nn as nn

# Define a simple model using GroupNorm
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv1 = nn.Conv2d(3, 64, kernel_size=3, padding=1)
        self.norm1 = nn.GroupNorm(num_groups=8, num_channels=64)

    def forward(self, x):
        x = self.conv1(x)
        x = self.norm1(x)
        return x

# Create an instance of the model and print its structure
model = SimpleModel()
print(model)