import torch
input_tensor = torch.randn(4, 5)
p_norm = 2
dim = 1
max_norm = 1.0
result = torch.renorm(input_tensor, p_norm, dim, max_norm)
print(result)