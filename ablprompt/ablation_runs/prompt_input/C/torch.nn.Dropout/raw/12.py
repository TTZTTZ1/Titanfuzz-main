import torch
from torch import nn

# Create a simple neural network with Dropout
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(784, 256)
        self.dropout = nn.Dropout(p=0.5)
        self.fc2 = nn.Linear(256, 10)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.dropout(x)  # Apply dropout
        x = self.fc2(x)
        return x

# Example usage
model = SimpleNet()
input_data = torch.randn(32, 784)  # Batch size of 32, 784 features
output = model(input_data)
print(output.shape)