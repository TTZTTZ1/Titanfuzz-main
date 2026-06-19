import torch

input_tensor = torch.randn(1, 3, 5)
output_size = (2,)
result = torch.nn.functional.adaptive_max_pool1d(input_tensor, output_size)