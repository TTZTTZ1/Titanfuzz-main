import torch
import torch.nn as nn

# Create a LeakyReLU layer with a custom negative slope
leaky_relu = nn.LeakyReLU(negative_slope=0.1)

# Define a simple neural network using LeakyReLU
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(10, 50)
        self.fc2 = nn.Linear(50, 2)

    def forward(self, x):
        x = leaky_relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Instantiate the network and an example input tensor
net = SimpleNet()
input_tensor = torch.randn(1, 10)

# Forward pass through the network
output = net(input_tensor)
print(output)