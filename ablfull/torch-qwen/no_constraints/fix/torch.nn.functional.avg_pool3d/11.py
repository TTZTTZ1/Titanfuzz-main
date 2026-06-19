import torch
input_tensor = torch.randn(1, 16, 32, 32, 32)
kernel_size = (2, 2, 2)
stride = (2, 2, 2)
output = torch.nn.functional.avg_pool3d(input_tensor, kernel_size, stride)