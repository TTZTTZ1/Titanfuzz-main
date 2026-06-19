import torch
import torch.nn as nn

# Define a simple model using ConvTranspose1d
class SimpleUpsampler(nn.Module):
    def __init__(self):
        super(SimpleUpsampler, self).__init__()
        self.conv_transpose = nn.ConvTranspose1d(in_channels=16, out_channels=8, kernel_size=5, stride=2, padding=1, output_padding=1)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and an input tensor
model = SimpleUpsampler()
input_tensor = torch.randn(1, 16, 32)  # Batch size 1, 16 input channels, sequence length 32

# Perform the forward pass
output_tensor = model(input_tensor)

print(output_tensor.shape)  # Expected output shape should be [1, 8, 67]