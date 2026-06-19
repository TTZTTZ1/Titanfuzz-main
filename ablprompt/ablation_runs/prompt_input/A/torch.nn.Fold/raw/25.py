import torch
from torch.nn import Fold

# Define input tensor and parameters for Fold operation
input_tensor = torch.randn(1, 32, 64, 64)  # Example input tensor of shape (batch_size, channels, height, width)
output_size = (16, 16)  # Desired output size
kernel_size = 4  # Size of each kernel
stride = 4  # Stride of the convolution
padding = 0  # Padding added to both sides of the input

# Create an instance of the Fold layer
fold_layer = Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding)

# Apply the Fold operation to the input tensor
output_tensor = fold_layer(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)