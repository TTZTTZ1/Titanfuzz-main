import torch
import torch.nn as nn

# Define a simple CNN model with MaxPool2d
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1)

    def forward(self, x):
        x = self.pool(self.conv1(x))
        x = self.pool(self.conv2(x))
        return x

# Create a random input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Initialize the model
model = SimpleCNN()

# Forward pass through the model
output_tensor = model(input_tensor)

print(output_tensor.shape)