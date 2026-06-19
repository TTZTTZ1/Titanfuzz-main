import torch
from torch import nn

# Define a simple model using Conv1d
class SimpleConv1dModel(nn.Module):
    def __init__(self):
        super(SimpleConv1dModel, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1, bias=True)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool1d(kernel_size=2)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)
        return x

# Create a random input tensor
input_tensor = torch.randn(20, 16, 50)

# Instantiate the model and run the input through it
model = SimpleConv1dModel()
output = model(input_tensor)

print(output.shape)  # Expected output shape: (20, 33, 24)