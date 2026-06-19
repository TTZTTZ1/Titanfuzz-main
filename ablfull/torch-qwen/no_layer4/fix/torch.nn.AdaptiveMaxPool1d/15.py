import torch
input_tensor = torch.randn(1, 64, 10)
output_size = 5
return_indices = False
result = torch.nn.AdaptiveMaxPool1d(output_size, return_indices)(input_tensor)