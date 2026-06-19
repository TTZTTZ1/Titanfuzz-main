import torch
input_data = torch.randn(1, 5, 64)
output_size = 8
return_indices = False
result = torch.nn.functional.adaptive_max_pool1d(input_data, output_size, return_indices)