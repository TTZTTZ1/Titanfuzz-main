import torch
from torch import nn

# Define a simple model using Conv2d
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=6, kernel_size=5)
    
    def forward(self, x):
        return self.conv1(x)

# Create an instance of the model and print its structure
model = SimpleCNN()
print(model)