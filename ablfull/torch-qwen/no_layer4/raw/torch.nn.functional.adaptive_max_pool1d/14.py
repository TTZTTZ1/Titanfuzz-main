import torch

input_tensor = torch.randn(1, 10)
output_size = 5
return_indices = False

result = torch.nn.functional.adaptive_max_pool1d(input_tensor, output_size, return_indices)