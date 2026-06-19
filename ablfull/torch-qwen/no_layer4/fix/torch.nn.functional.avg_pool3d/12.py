import torch
input_tensor = torch.randn(1, 1, 5, 5, 5)
output = torch.nn.functional.avg_pool3d(input_tensor, kernel_size=2, stride=2, padding=0, ceil_mode=False, count_include_pad=True)