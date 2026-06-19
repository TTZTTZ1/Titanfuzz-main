import torch
from torch.nn.modules import fold

# Define input tensor and parameters for Fold
input_tensor = torch.randn(1, 32, 8, 8)
output_size = (4, 4)
kernel_size = (2, 2)
stride = (2, 2)

# Create an instance of Fold
fold_layer = fold.Fold(output_size=output_size, kernel_size=kernel_size, stride=stride)

# Apply Fold to the input tensor
output_tensor = fold_layer(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)