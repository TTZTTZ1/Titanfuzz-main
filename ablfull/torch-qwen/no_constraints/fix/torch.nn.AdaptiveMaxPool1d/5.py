import torch
input_tensor = torch.randn(1, 64, 8)
output_size = 4
return_indices = False
result = torch.nn.AdaptiveMaxPool1d(output_size, return_indices)(input_tensor)