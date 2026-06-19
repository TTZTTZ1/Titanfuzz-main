import torch
import torch.nn as nn

# Define a simple 1D Convolutional Neural Network
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=1, out_channels=8, kernel_size=3, stride=1, padding=1)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool1d(kernel_size=2, stride=2)
        self.fc = nn.Linear(8 * 24, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)
        x = x.view(-1, 8 * 24)
        x = self.fc(x)
        return x

# Create an instance of the model and a random input tensor
model = SimpleCNN()
input_tensor = torch.randn(1, 1, 50)

# Forward pass through the model
output = model(input_tensor)
print(output.shape)  # Expected output shape: torch.Size([1, 10])