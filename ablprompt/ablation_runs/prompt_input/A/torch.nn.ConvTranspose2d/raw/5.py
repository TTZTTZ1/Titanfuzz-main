import torch
import torch.nn as nn

# Define a simple model using ConvTranspose2d
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv_transpose = nn.ConvTranspose2d(in_channels=1, out_channels=1, kernel_size=3, stride=2)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and a dummy input tensor
model = SimpleModel()
input_tensor = torch.randn(1, 1, 4, 4)  # Batch size 1, 1 channel, 4x4 image

# Forward pass through the model
output_tensor = model(input_tensor)

print(output_tensor.shape)