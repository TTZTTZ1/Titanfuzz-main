import torch
import torch.nn as nn
import torch.optim as optim

# Define a simple neural network using Tanh activation
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(784, 256)
        self.tanh = nn.Tanh()
        self.fc2 = nn.Linear(256, 10)

    def forward(self, x):
        x = self.fc1(x)
        x = self.tanh(x)
        x = self.fc2(x)
        return x

# Create an instance of the network and move it to GPU if available
net = SimpleNet().cuda() if torch.cuda.is_available() else SimpleNet()

# Dummy input data
input_data = torch.randn(1, 784).cuda() if torch.cuda.is_available() else torch.randn(1, 784)

# Forward pass through the network
output = net(input_data)

print(output)