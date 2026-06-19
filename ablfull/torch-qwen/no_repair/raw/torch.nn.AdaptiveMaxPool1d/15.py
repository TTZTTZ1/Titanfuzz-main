import torch

output_size = 2
return_indices = False
input_tensor = torch.randn(1, 4)

result = torch.nn.AdaptiveMaxPool1d(output_size, return_indices)(input_tensor)
print(result)