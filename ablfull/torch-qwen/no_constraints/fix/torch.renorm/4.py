import torch
x = torch.randn(3, 4)
p = 2
dim = 1
max_norm = 1.0
result = torch.renorm(x, p, dim, max_norm)
print(result)