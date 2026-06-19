import torch
import torch.nn as nn
import torch.optim as optim

# Define a simple neural network with Dropout
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(784, 256)
        self.dropout = nn.Dropout(p=0.5)
        self.fc2 = nn.Linear(256, 10)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.dropout(x)  # Apply dropout during training
        x = self.fc2(x)
        return x

# Create an instance of the network
net = SimpleNet()

# Dummy input tensor
input_tensor = torch.randn(1, 784)

# Forward pass
output = net(input_tensor)
print(output)