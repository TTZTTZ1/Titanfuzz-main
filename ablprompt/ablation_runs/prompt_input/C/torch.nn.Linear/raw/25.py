import torch
import torch.nn as nn

# Define a simple neural network with a single Linear layer
class SimpleNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

# Example usage
net = SimpleNet(input_size=784, hidden_size=512, output_size=10)
input_data = torch.randn(64, 784)  # Batch size of 64, 784 input features
output = net(input_data)
print(output.shape)  # Expected output shape: (64, 10)