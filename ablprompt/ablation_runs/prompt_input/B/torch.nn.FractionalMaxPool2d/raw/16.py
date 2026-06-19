import torch
import torch.nn.functional as F

# Create a random input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Define FractionalMaxPool2d parameters
kernel_size = (2, 2)
output_ratio = (0.5, 0.5)
return_indices = True

# Apply FractionalMaxPool2d
output, indices = F.fractional_max_pool2d(input_tensor, kernel_size, output_ratio=output_ratio, return_indices=return_indices)

print("Output Shape:", output.shape)
if return_indices:
    print("Indices Shape:", indices.shape)