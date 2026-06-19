import torch
import torch.nn as nn

# Define a simple 3D model using ConvTranspose3d
class Simple3DModel(nn.Module):
    def __init__(self):
        super(Simple3DModel, self).__init__()
        self.conv_transpose = nn.ConvTranspose3d(in_channels=16, out_channels=32, kernel_size=(3, 3, 3), stride=(2, 2, 2), padding=(1, 1, 1), output_padding=(0, 0, 0))

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and an input tensor
model = Simple3DModel()
input_tensor = torch.randn(1, 16, 8, 16, 32)

# Forward pass through the model
output_tensor = model(input_tensor)

print(output_tensor.shape)