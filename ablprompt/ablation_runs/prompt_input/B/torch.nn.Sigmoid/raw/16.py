import torch
import torch.nn as nn
import torch.optim as optim

# Define a simple neural network with Sigmoid activation
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(784, 256)
        self.sigmoid = nn.Sigmoid()
        self.fc2 = nn.Linear(256, 10)

    def forward(self, x):
        x = self.fc1(x)
        x = self.sigmoid(x)
        x = self.fc2(x)
        return x

# Create an instance of the network
net = SimpleNet()

# Dummy input data
input_data = torch.randn(1, 784)

# Forward pass through the network
output = net(input_data)
print(output)