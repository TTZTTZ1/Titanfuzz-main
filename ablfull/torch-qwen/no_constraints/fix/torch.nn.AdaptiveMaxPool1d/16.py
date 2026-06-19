import torch
input_tensor = torch.randn(1, 4, 5)
output_size = 2
return_indices = False
result = torch.nn.AdaptiveMaxPool1d(output_size, return_indices)(input_tensor)
print(result)