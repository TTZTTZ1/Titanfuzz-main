import torch

input_data = torch.randn(1, 4, 5)
output_size = 2
return_indices = False

result = torch.nn.functional.adaptive_max_pool1d(input_data, output_size, return_indices)