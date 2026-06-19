import torch

input_tensor = torch.randn(1, 10)
output_size = 5
adaptive_max_pool = torch.nn.AdaptiveMaxPool1d(output_size=output_size)
output = adaptive_max_pool(input_tensor)