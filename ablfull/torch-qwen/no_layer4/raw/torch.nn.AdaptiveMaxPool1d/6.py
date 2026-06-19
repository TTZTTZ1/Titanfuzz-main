import torch

output_size = (3,)
return_indices = True

x = torch.randn(1, 5)
result = torch.nn.AdaptiveMaxPool1d(output_size=output_size, return_indices=return_indices)(x)
print(result)