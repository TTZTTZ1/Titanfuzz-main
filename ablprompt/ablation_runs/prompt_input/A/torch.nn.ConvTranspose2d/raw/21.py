import torch
from torch import nn

# Define a simple model using ConvTranspose2d
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv_transpose = nn.ConvTranspose2d(in_channels=1, out_channels=1, kernel_size=3, stride=2, padding=1)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and input tensor
model = SimpleModel()
input_tensor = torch.randn(1, 1, 6, 6)  # Batch size of 1, 1 channel, 6x6 image

# Perform a forward pass
output_tensor = model(input_tensor)
print(output_tensor.shape)  # Expected output shape: [1, 1, 13, 13]