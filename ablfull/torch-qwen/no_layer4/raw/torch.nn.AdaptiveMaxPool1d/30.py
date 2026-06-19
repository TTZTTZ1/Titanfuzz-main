import torch

output_size = (2,)
return_indices = False

result = torch.nn.AdaptiveMaxPool1d(output_size=output_size, return_indices=return_indices)