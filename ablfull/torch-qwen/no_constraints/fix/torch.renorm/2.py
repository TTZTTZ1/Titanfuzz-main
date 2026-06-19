import torch
x = torch.randn(4, 4)
p = 2
dim = 0
maxnorm = 1.0
result = torch.renorm(x, p, dim, maxnorm)
print(result)