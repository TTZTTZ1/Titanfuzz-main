import torch
from torch import nn

# Define a simple model using Conv2d
class SimpleConvModel(nn.Module):
    def __init__(self):
        super(SimpleConvModel, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=(3, 3), stride=1, padding=1, bias=True)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=(2, 2), stride=2, padding=0)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)
        return x

# Create an instance of the model
model = SimpleConvModel()

# Example input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Forward pass through the model
output = model(input_tensor)

print(output.shape)