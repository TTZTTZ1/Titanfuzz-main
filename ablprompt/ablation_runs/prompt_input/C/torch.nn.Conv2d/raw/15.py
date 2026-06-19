import torch
import torch.nn as nn

# Define a simple model using Conv2d
class SimpleConvNet(nn.Module):
    def __init__(self):
        super(SimpleConvNet, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.conv2 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=1)
    
    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = self.pool(self.relu(self.conv2(x)))
        return x

# Create an instance of the model
model = SimpleConvNet()

# Example input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Forward pass through the model
output = model(input_tensor)

print(output.shape)  # Expected output shape: torch.Size([1, 128, 16, 16])