import torch
import torch.nn.functional as F

input_data = torch.randn(1, 1, 4, 4, 4)
kernel_size = 2
stride = 2
padding = 0
ceil_mode = False
count_include_pad = True

output = F.avg_pool3d(input_data, kernel_size, stride, padding, ceil_mode, count_include_pad)