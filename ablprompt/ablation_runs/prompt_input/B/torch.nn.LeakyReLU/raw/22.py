import torch
import torch.nn as nn

# Create a LeakyReLU layer with a custom negative slope
leaky_relu = nn.LeakyReLU(negative_slope=0.1)

# Define a simple neural network using LeakyReLU
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(784, 256)
        self.fc2 = nn.Linear(256, 10)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Initialize the network and move it to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
net = SimpleNet().to(device)

# Generate random input data
input_data = torch.randn(32, 784).to(device)

# Forward pass through the network
output = net(input_data)
print(output.shape)