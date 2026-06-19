import torch
from torch import nn

# Define a simple neural network using Linear layers
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(784, 128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return x

# Create an instance of the network
net = SimpleNet()

# Example input tensor
input_tensor = torch.randn(1, 784)

# Forward pass
output = net(input_tensor)
print(output.shape)  # Expected shape: (1, 10)