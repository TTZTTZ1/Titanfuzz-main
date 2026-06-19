import torch
from torch.nn import Conv1d

# Create a random input tensor
input_tensor = torch.randn(32, 16, 50)

# Define the convolutional layer
conv_layer = Conv1d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1, groups=1, bias=True, padding_mode='zeros')

# Apply the convolutional layer to the input tensor
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)