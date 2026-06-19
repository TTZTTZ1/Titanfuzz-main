import torch

input_tensor = torch.randn(3, 4)
p = 2.0
dim = 1
maxnorm = 1.5

output_tensor = torch.renorm(input_tensor, p, dim, maxnorm)