import torch
import torch.nn.functional as F

# Create a random input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Define the FractionalMaxPool2d layer
fractional_max_pool = F.max_pool2d(input_tensor, kernel_size=3, stride=2, padding=1, dilation=1, ceil_mode=False)

# Apply the FractionalMaxPool2d layer to the input tensor
output_tensor = fractional_max_pool(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)