import torch

input_tensor = torch.randn(1, 4, 5)
output_size = 3
adaptive_max_pool = torch.nn.AdaptiveMaxPool1d(output_size=output_size)
result = adaptive_max_pool(input_tensor)
print(result)