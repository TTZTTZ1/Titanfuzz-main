import torch
import torch.nn as nn

# Create a Tanh activation function
tanh = nn.Tanh()

# Define a simple neural network with a single Tanh layer
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc = nn.Linear(10, 5)
        self.tanh = nn.Tanh()
        self.fc2 = nn.Linear(5, 1)

    def forward(self, x):
        x = self.fc(x)
        x = self.tanh(x)
        x = self.fc2(x)
        return x

# Initialize the network
net = SimpleNet()

# Generate random input data
input_data = torch.randn(32, 10)

# Forward pass through the network
output = net(input_data)

print(output)