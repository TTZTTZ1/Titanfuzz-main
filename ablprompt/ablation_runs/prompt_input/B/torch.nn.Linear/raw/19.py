import torch
import torch.nn as nn

# Define a simple neural network model using torch.nn.Linear
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

# Create an instance of the model and move it to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = SimpleNet().to(device)

# Example input tensor
input_tensor = torch.randn(1, 784).to(device)

# Forward pass through the model
output = model(input_tensor)
print(output.shape)  # Expected shape: [1, 10]