import torch
output_size = 5
return_indices = False
input_tensor = torch.randn(1, 10)
result = torch.nn.AdaptiveMaxPool1d(output_size=output_size, return_indices=return_indices)(input_tensor)