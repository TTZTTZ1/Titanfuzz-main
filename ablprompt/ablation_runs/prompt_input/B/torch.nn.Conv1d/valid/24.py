import torch
from torch import nn

# Define a simple model with Conv1d
class SimpleConv1dModel(nn.Module):
    def __init__(self):
        super(SimpleConv1dModel, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1, groups=1, bias=True, padding_mode='zeros')
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        return x

# Create a random input tensor
input_tensor = torch.randn(20, 16, 50)

# Initialize the model
model = SimpleConv1dModel()

# Forward pass through the model
output_tensor = model(input_tensor)

print(output_tensor.shape)  # Expected output shape: (20, 33, 24)