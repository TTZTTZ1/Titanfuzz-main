import torch
import torch.nn as nn

# Create a simple neural network model
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(784, 256)
        self.dropout = nn.Dropout(p=0.3)
        self.fc2 = nn.Linear(256, 10)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.dropout(x)  # Apply dropout
        x = self.fc2(x)
        return x

# Initialize the model
model = SimpleNet()

# Example input tensor
input_tensor = torch.randn(1, 784)

# Forward pass through the model
output = model(input_tensor)
print(output)