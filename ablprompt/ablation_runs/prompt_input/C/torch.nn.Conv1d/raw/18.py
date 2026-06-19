import torch
import torch.nn as nn

# Define a simple model using Conv1d
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=1, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool1d(kernel_size=2, stride=2)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)
        return x

# Create an instance of the model
model = SimpleCNN()

# Dummy input tensor
input_tensor = torch.randn(1, 1, 100)  # Batch size 1, 1 channel, sequence length 100

# Forward pass
output = model(input_tensor)
print(output.shape)  # Expected output shape: torch.Size([1, 32, 50])