
import torch
input_tensor = torch.randn(4, 5, requires_grad=True)
p = 2.0
dim = 1
maxnorm = 1.0
result = torch.renorm(input_tensor, p, dim, maxnorm)
print(result)
