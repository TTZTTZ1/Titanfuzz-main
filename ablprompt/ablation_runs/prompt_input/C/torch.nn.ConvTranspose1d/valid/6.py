import torch
import torch.nn as nn

# Define a simple model using ConvTranspose1d
class SimpleUpsampler(nn.Module):
    def __init__(self):
        super(SimpleUpsampler, self).__init__()
        self.conv_transpose = nn.ConvTranspose1d(in_channels=1, out_channels=1, kernel_size=4, stride=2, padding=1)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model
model = SimpleUpsampler()

# Example input tensor
input_tensor = torch.randn(1, 1, 5)  # Batch size of 1, 1 channel, sequence length of 5

# Forward pass through the model
output_tensor = model(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)