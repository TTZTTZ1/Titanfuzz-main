import torch
import torch.nn as nn

# Define a simple neural network with Linear layers
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(784, 256)
        self.fc2 = nn.Linear(256, 128)
        self.fc3 = nn.Linear(128, 10)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# Create an instance of the network
net = SimpleNet()

# Example input tensor
input_tensor = torch.randn(1, 784)

# Forward pass through the network
output = net(input_tensor)
print(output.shape)  # Expected shape: torch.Size([1, 10])