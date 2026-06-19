import torch
input_tensor = torch.randn(1, 3, 5, 5, 5)
kernel_size = 2
stride = 2
padding = 0
ceil_mode = False
count_include_pad = True
divisor_override = None
output_tensor = torch.nn.functional.avg_pool3d(input_tensor, kernel_size, stride, padding, ceil_mode, count_include_pad, divisor_override)