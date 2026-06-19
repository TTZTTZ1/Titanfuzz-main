import torch
input_data = torch.randn(1, 64, 50)
output_size = 10
return_indices = False
result = torch.nn.functional.adaptive_max_pool1d(input_data, output_size, return_indices)