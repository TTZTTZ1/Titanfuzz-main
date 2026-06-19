import torch

input_tensor = torch.randn(1, 5, 6)
output_size = (4,)
adaptive_max_pool = torch.nn.AdaptiveMaxPool1d(output_size)
output = adaptive_max_pool(input_tensor)