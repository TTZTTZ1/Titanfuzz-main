import torch

output_size = 5
return_indices = True

input_tensor = torch.randn(1, 64, 8)
result = torch.nn.AdaptiveMaxPool1d(output_size, return_indices)(input_tensor)
print(result)