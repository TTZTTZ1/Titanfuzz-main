import torch
import torch.nn as nn

# Define a simple neural network with multiple Linear layers
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(in_features=784, out_features=256)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(in_features=256, out_features=10)
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Create an instance of the network
net = SimpleNet()

# Example input tensor
input_tensor = torch.randn(1, 784)

# Forward pass through the network
output = net(input_tensor)
print(output.shape)  # Expected shape: [1, 10]