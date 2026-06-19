import torch
from torch.nn import Unfold

# Create a random input tensor
input_tensor = torch.randn(1, 1, 5, 5)

# Define the parameters for Unfold
kernel_size = (2, 2)
stride = (1, 1)
padding = (1, 1)
dilation = (1, 1)

# Initialize the Unfold layer
unfold = Unfold(kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)

# Apply Unfold to the input tensor
output_tensor = unfold(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)
print("Output Tensor:\n", output_tensor)