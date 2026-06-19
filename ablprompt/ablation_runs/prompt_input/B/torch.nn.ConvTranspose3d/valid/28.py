import torch
import torch.nn as nn

# Define a simple 3D model using ConvTranspose3d
class Simple3DModel(nn.Module):
    def __init__(self):
        super(Simple3DModel, self).__init__()
        self.conv_transpose = nn.ConvTranspose3d(in_channels=16, out_channels=32, kernel_size=3, stride=2, padding=1, output_padding=1)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and a random input tensor
model = Simple3DModel()
input_tensor = torch.randn(1, 16, 10, 10, 10)

# Forward pass through the model
output_tensor = model(input_tensor)

print(output_tensor.shape)  # Expected shape: [1, 32, 20, 20, 20]