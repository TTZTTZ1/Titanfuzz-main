import torch
from torch import nn

# Define a simple neural network model using Linear layers
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

# Create an instance of the model
model = SimpleNet()

# Example input tensor
input_tensor = torch.randn(64, 784)

# Forward pass through the model
output = model(input_tensor)
print(output.shape)  # Expected shape: (64, 10)