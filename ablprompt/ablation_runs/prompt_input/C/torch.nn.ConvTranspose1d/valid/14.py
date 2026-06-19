import torch
import torch.nn as nn

# Define a simple model using ConvTranspose1d
class SimpleUpsampler(nn.Module):
    def __init__(self):
        super(SimpleUpsampler, self).__init__()
        self.conv_transpose = nn.ConvTranspose1d(in_channels=16, out_channels=8, kernel_size=3, stride=2, padding=1)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model
model = SimpleUpsampler()

# Generate random input data
input_data = torch.randn(1, 16, 32)  # Batch size of 1, 16 input channels, sequence length of 32

# Forward pass through the model
output_data = model(input_data)

print(output_data.shape)  # Expected output shape: [1, 8, 64]