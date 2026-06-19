import torch

# Prepare input data
input_tensor = torch.randn(1, 1, 5, 5, 5)

# Define parameters
kernel_size = 3
stride = 1
padding = 1
ceil_mode = False
count_include_pad = True
divisor_override = None

# Call the API
output = torch.nn.functional.avg_pool3d(input_tensor, kernel_size=kernel_size, stride=stride, padding=padding, ceil_mode=ceil_mode, count_include_pad=count_include_pad, divisor_override=divisor_override)