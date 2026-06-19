import torch
x = torch.randn(5, 3)
p = 2
dim = 1
max_norm = 1.0
result = torch.renorm(x, p, dim, max_norm)
print(result)