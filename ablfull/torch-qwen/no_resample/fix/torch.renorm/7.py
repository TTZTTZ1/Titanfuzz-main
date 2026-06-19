import torch
input_tensor = torch.tensor([[1.0, (- 2.0)], [(- 3.0), 4.0]])
p = 2.0
dim = 1
maxnorm = 2.0
result = torch.renorm(input_tensor, p, dim, maxnorm)