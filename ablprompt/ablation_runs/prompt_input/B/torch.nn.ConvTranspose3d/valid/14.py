import torch
from torch import nn

# Define a simple model using ConvTranspose3d
class SimpleUpsampler(nn.Module):
    def __init__(self):
        super(SimpleUpsampler, self).__init__()
        self.conv_transpose = nn.ConvTranspose3d(in_channels=16, out_channels=32, kernel_size=(3, 3, 3), stride=(2, 2, 2), padding=(1, 1, 1))

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and an input tensor
model = SimpleUpsampler()
input_tensor = torch.randn(1, 16, 10, 50, 100)

# Perform the forward pass
output_tensor = model(input_tensor)

print(output_tensor.shape)  # Output should be (1, 32, 20, 100, 200)