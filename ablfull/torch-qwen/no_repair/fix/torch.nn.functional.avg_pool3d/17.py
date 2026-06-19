
import torch
input_tensor = torch.randn(1, 3, 8, 8, 8)
output = torch.nn.functional.avg_pool3d(input_tensor, kernel_size=2, stride=2, padding=1)
