import torch
x = torch.randn(3, 4)
p = 2
dim = 0
maxnorm = 1.5
result = torch.renorm(x, p, dim, maxnorm)