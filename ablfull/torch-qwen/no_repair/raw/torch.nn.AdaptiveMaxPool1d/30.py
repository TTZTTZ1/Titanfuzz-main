import torch

output_size = 5
return_indices = False

x = torch.randn(1, 64)
result = torch.nn.AdaptiveMaxPool1d(output_size, return_indices)(x)