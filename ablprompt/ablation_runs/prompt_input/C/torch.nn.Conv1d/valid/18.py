import torch
import torch.nn as nn

# Define a simple model using Conv1d
class SimpleConv1dModel(nn.Module):
    def __init__(self):
        super(SimpleConv1dModel, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool1d(kernel_size=2)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)
        return x

# Create a random input tensor
input_tensor = torch.randn(20, 16, 50)

# Initialize the model
model = SimpleConv1dModel()

# Forward pass through the model
output_tensor = model(input_tensor)

print(output_tensor.shape)  # Expected shape: (20, 33, 24)