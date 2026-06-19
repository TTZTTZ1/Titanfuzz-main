
import torch
input_tensor = torch.randn(1, 1, 5, 5, 5)
kernel_size = 3
stride = 1
padding = 1
ceil_mode = False
count_include_pad = True
divisor_override = None
output = torch.nn.functional.avg_pool3d(input_tensor, kernel_size=kernel_size, stride=stride, padding=padding, ceil_mode=ceil_mode, count_include_pad=count_include_pad, divisor_override=divisor_override)
