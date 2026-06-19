
import torch
input_tensor = torch.randn(1, 5)
output_size = 3
return_indices = False
result = torch.nn.AdaptiveMaxPool1d(output_size, return_indices)(input_tensor)
