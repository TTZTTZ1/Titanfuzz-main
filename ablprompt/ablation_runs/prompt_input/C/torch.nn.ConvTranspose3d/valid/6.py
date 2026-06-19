import torch
import torch.nn as nn

# Define a simple model using ConvTranspose3d
class SimpleUpsampler(nn.Module):
    def __init__(self):
        super(SimpleUpsampler, self).__init__()
        self.conv_transpose = nn.ConvTranspose3d(in_channels=1, out_channels=1, kernel_size=3, stride=2, padding=1, output_padding=1)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and an input tensor
model = SimpleUpsampler()
input_tensor = torch.randn(1, 1, 8, 8, 8)

# Perform the forward pass
output_tensor = model(input_tensor)

print(output_tensor.shape)  # Expected output shape should be (1, 1, 15, 15, 15)