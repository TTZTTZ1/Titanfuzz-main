import torch
import torch.nn as nn
import torch.optim as optim

# Define a simple convolutional neural network
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1)
        self.bn1 = nn.BatchNorm2d(32)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.bn2 = nn.BatchNorm2d(64)
        self.fc = nn.Linear(64 * 7 * 7, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = torch.relu(x)
        x = self.conv2(x)
        x = self.bn2(x)
        x = torch.relu(x)
        x = x.view(-1, 64 * 7 * 7)
        x = self.fc(x)
        return x

# Create an instance of the model
model = SimpleCNN()

# Dummy input tensor
input_tensor = torch.randn(16, 1, 28, 28)

# Forward pass
output = model(input_tensor)

# Print output shape
print(output.shape)