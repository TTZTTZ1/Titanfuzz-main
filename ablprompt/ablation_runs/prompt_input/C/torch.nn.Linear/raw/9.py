import torch
import torch.nn as nn

# Define a simple neural network with a single Linear layer
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc = nn.Linear(in_features=784, out_features=10, bias=True)

    def forward(self, x):
        return self.fc(x)

# Create an instance of the network
net = SimpleNet()

# Example input tensor
input_tensor = torch.randn(64, 784)

# Forward pass through the network
output = net(input_tensor)

print(output.shape)  # Should be (64, 10)