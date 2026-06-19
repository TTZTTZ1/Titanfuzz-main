import torch
import torch.nn as nn

# Define a simple neural network with a Linear layer
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(in_features=784, out_features=128)
        self.fc2 = nn.Linear(in_features=128, out_features=64)
        self.fc3 = nn.Linear(in_features=64, out_features=10)

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
print(output.shape)  # Should be torch.Size([1, 10])