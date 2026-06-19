import torch
input_data = torch.randn(1, 3, 5)
output_size = (2,)
return_indices = False
result = torch.nn.AdaptiveMaxPool1d(output_size, return_indices)(input_data)