import torch
import torch.nn.functional as F

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define the FractionalMaxPool2d layer
fractional_max_pool = F.max_pool2d

# Apply the layer with specific parameters
output_tensor = fractional_max_pool(input_tensor, kernel_size=3, stride=2, padding=1, dilation=1, ceil_mode=False)

print(output_tensor.shape)