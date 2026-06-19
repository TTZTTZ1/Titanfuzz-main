import torch
import torch.nn as nn

# Define a simple neural network with LayerNorm
class SimpleNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.ln1 = nn.LayerNorm(hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.ln1(x)
        x = self.fc2(x)
        return x

# Create an instance of the network
net = SimpleNet(784, 256, 10)

# Example input
input_data = torch.randn(32, 784)

# Forward pass
output = net(input_data)
print(output.shape)  # Should be [32, 10]