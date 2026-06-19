import torch

# Prepare valid input data
input_tensor = torch.randn(1, 1, 5, 5, 5)
kernel_size = 3
stride = 1
padding = 1
ceil_mode = False
count_include_pad = True
divisor_override = None

# Call the API
output = torch.nn.functional.avg_pool3d(input_tensor, kernel_size, stride, padding, ceil_mode, count_include_pad, divisor_override)