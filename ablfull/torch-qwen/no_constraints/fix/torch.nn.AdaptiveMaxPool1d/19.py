import torch
input_tensor = torch.randn(1, 64, 8)
output_size = 4
return_indices = True
result = torch.nn.AdaptiveMaxPool1d(output_size=output_size, return_indices=return_indices)(input_tensor)