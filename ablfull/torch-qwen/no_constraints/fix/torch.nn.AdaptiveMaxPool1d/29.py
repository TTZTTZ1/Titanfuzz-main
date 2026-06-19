import torch
input_tensor = torch.randn(1, 3, 5)
output_size = (2,)
adaptive_max_pool = torch.nn.AdaptiveMaxPool1d(output_size)
result = adaptive_max_pool(input_tensor)