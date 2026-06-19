import torch
import torch.nn as nn

# Create a LeakyReLU layer with a custom slope
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
net = SimpleNet().cuda() if torch.cuda.is_available() else SimpleNet()

# Generate random input data
input_data = torch.randn(32, 784).cuda() if torch.cuda.is_available() else torch.randn(32, 784)

# Forward pass through the network
output = net(input_data)

# Apply LeakyReLU to the output
output_with_leaky_relu = leaky_relu(output)

print(output_with_leaky_relu.shape)