import torch
input_tensor = torch.randn(3, 4)
p_norm = 2
max_norm = 1.0
result = torch.renorm(input_tensor, p_norm, dim=1, maxnorm=max_norm)
print(result)