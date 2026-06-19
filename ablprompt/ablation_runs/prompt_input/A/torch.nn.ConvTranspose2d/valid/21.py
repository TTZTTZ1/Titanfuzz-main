import torch
import torch.nn as nn

# Define a simple model using ConvTranspose2d
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv_transpose = nn.ConvTranspose2d(in_channels=1, out_channels=3, kernel_size=3, stride=2)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and input tensor
model = SimpleModel()
input_tensor = torch.randn(1, 1, 6, 6)  # Batch size 1, 1 channel, 6x6 image

# Forward pass through the model
output_tensor = model(input_tensor)
print(output_tensor.shape)  # Expected output shape: [1, 3, 13, 13]