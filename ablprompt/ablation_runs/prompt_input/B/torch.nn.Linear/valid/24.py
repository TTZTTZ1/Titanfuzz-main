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

# Create an instance of the network and move it to GPU if available
net = SimpleNet().cuda() if torch.cuda.is_available() else SimpleNet()

# Generate random input data
input_data = torch.randn(64, 784).cuda() if torch.cuda.is_available() else torch.randn(64, 784)

# Forward pass through the network
output = net(input_data)

print(output.shape)  # Expected shape: (64, 10)