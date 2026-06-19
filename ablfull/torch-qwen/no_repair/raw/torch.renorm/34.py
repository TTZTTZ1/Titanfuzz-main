import torch

input_tensor = torch.randn(4, 3)
p_norm = 2.0
dimension = 1
max_norm_value = 1.0

result = torch.renorm(input_tensor, p=p_norm, dim=dimension, maxnorm=max_norm_value)