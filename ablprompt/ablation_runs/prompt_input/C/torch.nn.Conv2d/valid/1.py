import torch
from torch import nn

# Define a simple CNN model using Conv2d
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1)
    
    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)
        x = self.conv2(x)
        return x

# Create an instance of the model
model = SimpleCNN()

# Example input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Forward pass
output = model(input_tensor)
print(output.shape)  # Expected output shape: torch.Size([1, 32, 16, 16])