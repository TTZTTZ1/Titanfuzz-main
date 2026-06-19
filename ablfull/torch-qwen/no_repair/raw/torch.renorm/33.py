import torch

input_tensor = torch.tensor([[1.0, -1.0], [-1.0, 1.0]])
p = 2.0
dim = 1
maxnorm = 1.5

result = torch.renorm(input_tensor, p, dim, maxnorm)
print(result)