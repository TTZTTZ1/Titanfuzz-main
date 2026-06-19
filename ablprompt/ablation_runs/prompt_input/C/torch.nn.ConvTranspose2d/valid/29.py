import torch
import torch.nn as nn

# Define a simple model using ConvTranspose2d
class UpsampleModel(nn.Module):
    def __init__(self):
        super(UpsampleModel, self).__init__()
        self.conv_transpose = nn.ConvTranspose2d(in_channels=1, out_channels=1, kernel_size=4, stride=2, padding=1)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and a random input tensor
model = UpsampleModel()
input_tensor = torch.randn(1, 1, 32, 32)

# Perform the forward pass
output_tensor = model(input_tensor)

print(output_tensor.shape)