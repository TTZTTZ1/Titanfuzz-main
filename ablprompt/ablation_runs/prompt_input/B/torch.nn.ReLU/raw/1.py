import torch
import torch.nn as nn

# Create a simple neural network with ReLU activation
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(784, 256)
        self.relu = nn.ReLU(inplace=True)
        self.fc2 = nn.Linear(256, 10)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Example usage
net = SimpleNet()
input_tensor = torch.randn(1, 784)
output = net(input_tensor)
print(output)