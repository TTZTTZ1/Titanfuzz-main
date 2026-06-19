import torch
import torch.nn as nn

# Define a simple model using ConvTranspose3d
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv_transpose = nn.ConvTranspose3d(in_channels=1, out_channels=1, kernel_size=(2, 2, 2), stride=(2, 2, 2))

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and input tensor
model = SimpleModel()
input_tensor = torch.randn(1, 1, 4, 4, 4)  # Batch size 1, channels 1, spatial dimensions 4x4x4

# Perform a forward pass
output_tensor = model(input_tensor)
print(output_tensor.shape)  # Expected output shape: torch.Size([1, 1, 8, 8, 8])