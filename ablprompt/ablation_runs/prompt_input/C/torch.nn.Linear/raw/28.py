import torch
import torch.nn as nn

# Define a simple model with multiple Linear layers
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(in_features=784, out_features=256)
        self.fc2 = nn.Linear(in_features=256, out_features=128)
        self.fc3 = nn.Linear(in_features=128, out_features=10)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# Create an instance of the model
model = SimpleModel()

# Example input tensor
input_tensor = torch.randn(64, 784)

# Forward pass through the model
output = model(input_tensor)

print(output.shape)  # Expected shape: (64, 10)