import torch
import torch.nn as nn

# Define a simple model using ConvTranspose2d
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv_transpose = nn.ConvTranspose2d(in_channels=1, out_channels=1, kernel_size=3, stride=1, padding=1)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and run it
model = SimpleModel()
input_tensor = torch.randn(1, 1, 4, 4)  # Batch size of 1, 1 channel, 4x4 image
output_tensor = model(input_tensor)
print(output_tensor.shape)  # Expected output shape: [1, 1, 4, 4]