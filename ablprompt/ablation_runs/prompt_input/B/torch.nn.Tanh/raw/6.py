import torch
import torch.nn as nn

# Create a Tanh activation layer
tanh = nn.Tanh()

# Define a simple neural network with Tanh activation
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(10, 20)
        self.tanh = nn.Tanh()
        self.fc2 = nn.Linear(20, 1)

    def forward(self, x):
        x = self.fc1(x)
        x = self.tanh(x)
        x = self.fc2(x)
        return x

# Create an instance of the network
net = SimpleNet()

# Example input
input_tensor = torch.randn(5, 10)

# Forward pass through the network
output = net(input_tensor)

print(output)