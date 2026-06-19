import torch
import torch.nn as nn

# Create a Tanh activation layer
tanh = nn.Tanh()

# Define a simple neural network with a single hidden layer
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(784, 256)
        self.fc2 = nn.Linear(256, 10)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = tanh(x)
        x = self.fc2(x)
        return x

# Instantiate the network and move it to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
net = SimpleNet().to(device)

# Example input data
input_data = torch.randn(32, 784).to(device)

# Forward pass through the network
output = net(input_data)
print(output.shape)  # Should be [32, 10]