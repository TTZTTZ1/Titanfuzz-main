import torch
import torch.nn.functional as F
input_tensor = torch.randn(1, 3, 4, 4, 4)
output_tensor = F.avg_pool3d(input_tensor, kernel_size=2)