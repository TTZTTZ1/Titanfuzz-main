import torch
from torch import nn

# Define a simple model using ConvTranspose3d
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv_transpose = nn.ConvTranspose3d(in_channels=1, out_channels=1, kernel_size=(2, 2, 2), stride=(1, 1, 1))

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and input tensor
model = SimpleModel()
input_tensor = torch.randn(1, 1, 4, 4, 4)  # Batch size of 1, 1 channel, 4x4x4 spatial dimensions

# Perform a forward pass
output_tensor = model(input_tensor)
print(output_tensor.shape)  # Output should be [1, 1, 5, 5, 5]