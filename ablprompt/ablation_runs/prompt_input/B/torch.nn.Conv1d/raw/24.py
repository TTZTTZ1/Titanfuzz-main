import torch
from torch import nn

# Define a simple model with Conv1d layer
class SimpleConv1dModel(nn.Module):
    def __init__(self):
        super(SimpleConv1dModel, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1, bias=True)
    
    def forward(self, x):
        return self.conv1(x)

# Create an instance of the model
model = SimpleConv1dModel()

# Generate random input tensor
input_tensor = torch.randn(20, 16, 50)

# Forward pass through the model
output_tensor = model(input_tensor)

print(output_tensor.shape)  # Expected output shape: (20, 33, 24)