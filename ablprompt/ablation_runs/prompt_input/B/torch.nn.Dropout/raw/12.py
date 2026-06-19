import torch
import torch.nn as nn

# Create a simple neural network with dropout
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

# Initialize the model and move to GPU if available
model = SimpleNet().cuda() if torch.cuda.is_available() else SimpleNet()

# Example input
input_data = torch.randn(32, 784).cuda() if torch.cuda.is_available() else torch.randn(32, 784)

# Forward pass
output = model(input_data)
print(output.shape)