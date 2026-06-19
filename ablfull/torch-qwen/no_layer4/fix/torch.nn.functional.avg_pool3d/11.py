import torch
input_tensor = torch.randn(1, 1, 5, 5, 5)
output_tensor = torch.nn.functional.avg_pool3d(input_tensor, kernel_size=3, stride=2, padding=1)