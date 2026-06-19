import torch
input_tensor = torch.randn(1, 3, 5, 5, 5)
kernel_size = (2, 2, 2)
stride = (1, 1, 1)
output_tensor = torch.nn.functional.avg_pool3d(input_tensor, kernel_size, stride)