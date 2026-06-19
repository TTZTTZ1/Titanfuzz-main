import torch
input_tensor = torch.randn(5, 3)
p = 2
dim = 0
max_norm = 1.0
result = torch.renorm(input_tensor, p, dim, max_norm)
print(result)