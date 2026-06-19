import torch
from torch import nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define FractionalMaxPool2d parameters
frac_pool = nn.FractionalMaxPool2d(output_size=(16, 16), fractional_stride=(0.5, 0.5))

# Apply the FractionalMaxPool2d operation
output_tensor = frac_pool(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)