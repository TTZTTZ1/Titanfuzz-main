import torch
from torch import nn

# Define a simple 3D model using ConvTranspose3d
class Simple3DModel(nn.Module):
    def __init__(self):
        super(Simple3DModel, self).__init__()
        self.conv_transpose = nn.ConvTranspose3d(in_channels=16, out_channels=33, kernel_size=(3, 3, 3), stride=(2, 2, 2), padding=(1, 1, 1))

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model
model = Simple3DModel()

# Generate a random input tensor
input_tensor = torch.randn(1, 16, 10, 50, 100)

# Perform the forward pass
output_tensor = model(input_tensor)

print(output_tensor.shape)