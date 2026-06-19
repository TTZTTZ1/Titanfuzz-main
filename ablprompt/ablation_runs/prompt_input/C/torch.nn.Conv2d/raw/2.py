import torch
from torch import nn

# Define a simple model using Conv2d
class SimpleConvModel(nn.Module):
    def __init__(self):
        super(SimpleConvModel, self).__init__()
        self.conv_layer = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=True)

    def forward(self, x):
        return self.conv_layer(x)

# Create an instance of the model
model = SimpleConvModel()

# Example input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Forward pass through the model
output_tensor = model(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 64, 32, 32])