import torch
import torch.nn as nn

# Define a simple model using ConvTranspose2d for upsampling
class UpsampleNet(nn.Module):
    def __init__(self):
        super(UpsampleNet, self).__init__()
        self.conv_transpose = nn.ConvTranspose2d(in_channels=3, out_channels=64, kernel_size=4, stride=2, padding=1)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and input tensor
model = UpsampleNet()
input_tensor = torch.randn(1, 3, 32, 32)

# Perform the forward pass
output_tensor = model(input_tensor)

print(output_tensor.shape)  # Expected shape: torch.Size([1, 64, 64, 64])