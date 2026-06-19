import torch

input_tensor = torch.randn(1, 3, 4, 4, 4)
kernel_size = 2
stride = 2
padding = 0

output_tensor = torch.nn.functional.avg_pool3d(input_tensor, kernel_size, stride, padding)