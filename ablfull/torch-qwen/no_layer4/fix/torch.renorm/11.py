import torch
input_tensor = torch.randn(4, 3, 2)
p = 2.0
dim = 1
maxnorm = 1.0
result = torch.renorm(input_tensor, p, dim, maxnorm)