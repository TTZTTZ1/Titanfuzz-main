import torch
from torch.nn import Fold

# Define input tensor and parameters for Fold
input_tensor = torch.randn(1, 3, 4, 4)
output_size = (2, 2)
kernel_size = (2, 2)
stride = (2, 2)

# Create an instance of Fold
fold = Fold(output_size=output_size, kernel_size=kernel_size, stride=stride)

# Apply Fold to the input tensor
output_tensor = fold(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)