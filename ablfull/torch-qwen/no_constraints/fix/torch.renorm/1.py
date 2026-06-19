import torch
input_tensor = torch.randn(3, 4)
p_norm = 2
dim = 0
max_norm = 1.0
result = torch.renorm(input_tensor, p_norm, dim, max_norm)
print(result)