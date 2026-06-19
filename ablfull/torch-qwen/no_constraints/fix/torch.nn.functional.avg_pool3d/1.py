import torch
input_tensor = torch.randn(1, 3, 4, 5, 6)
output_tensor = torch.nn.functional.avg_pool3d(input_tensor, kernel_size=2)