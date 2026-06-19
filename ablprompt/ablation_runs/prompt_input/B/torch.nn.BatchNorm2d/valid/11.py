import torch
import torch.nn as nn
import torch.optim as optim

# Define a simple CNN model with BatchNorm2d
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(32)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc1 = nn.Linear(32 * 14 * 14, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.pool(x)
        x = x.view(-1, 32 * 14 * 14)
        x = self.fc1(x)
        return x

# Create an instance of the model
model = SimpleCNN()

# Dummy input tensor
input_tensor = torch.randn(64, 1, 28, 28)

# Forward pass
output = model(input_tensor)

# Print output shape
print(output.shape)