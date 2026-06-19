import torch

input_tensor = torch.randn(1, 3, 4, 4, 4)
kernel_size = 2
stride = 2
padding = 0
ceil_mode = False
count_include_pad = True
divisor_override = None

output = torch.nn.functional.avg_pool3d(input_tensor, kernel_size, stride, padding, ceil_mode, count_include_pad, divisor_override)