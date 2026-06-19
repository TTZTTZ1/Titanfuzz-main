import torch
from torch import nn

# Create a Conv1d layer with specific parameters
conv_layer = nn.Conv1d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1, bias=True)

# Generate a random input tensor
input_tensor = torch.randn(20, 16, 50)

# Apply the convolutional layer to the input tensor
output_tensor = conv_layer(input_tensor)

# Print the shapes of the input and output tensors
print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)