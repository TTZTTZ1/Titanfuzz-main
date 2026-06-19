import torch
x = torch.randn(4, 5)
p = 2
dim = 1
max_norm = 0.5
result = torch.renorm(x, p, dim, max_norm)
print(result)