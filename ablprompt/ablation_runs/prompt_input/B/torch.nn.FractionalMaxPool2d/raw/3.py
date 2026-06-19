import torch
import torch.nn.functional as F

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define FractionalMaxPool2d parameters
kernel_size = (3, 3)
output_size = (16, 16)
return_indices = True

# Apply FractionalMaxPool2d
output, indices = F.fractional_max_pool2d(input_tensor, kernel_size, output_size=output_size, return_indices=return_indices)

print("Output shape:", output.shape)
if return_indices:
    print("Indices shape:", indices.shape)