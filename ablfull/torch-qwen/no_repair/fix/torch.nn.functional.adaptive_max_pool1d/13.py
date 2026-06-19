
import torch
input_tensor = torch.randn(1, 64)
output = torch.nn.functional.adaptive_max_pool1d(input_tensor, output_size=8)
