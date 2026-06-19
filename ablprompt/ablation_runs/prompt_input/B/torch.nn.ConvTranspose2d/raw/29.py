import torch
import torch.nn as nn

# Create a ConvTranspose2d layer
m = nn.ConvTranspose2d(in_channels=16, out_channels=33, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), output_padding=(0, 0), groups=1, bias=True, dilation=(1, 1))

# Create a random input tensor
input_tensor = torch.randn(20, 16, 50, 100)

# Apply the convolutional transpose operation
output_tensor = m(input_tensor)

print(output_tensor.shape)