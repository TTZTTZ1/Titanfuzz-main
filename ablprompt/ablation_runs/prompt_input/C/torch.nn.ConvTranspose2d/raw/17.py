import torch
import torch.nn as nn

# Define a simple model using ConvTranspose2d
class SimpleUpsampler(nn.Module):
    def __init__(self):
        super(SimpleUpsampler, self).__init__()
        self.conv_transpose = nn.ConvTranspose2d(in_channels=3, out_channels=64, kernel_size=4, stride=2, padding=1)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and run it on a dummy input
model = SimpleUpsampler()
dummy_input = torch.randn(1, 3, 32, 32)
output = model(dummy_input)
print(output.shape)  # Expected shape: torch.Size([1, 64, 64, 64])