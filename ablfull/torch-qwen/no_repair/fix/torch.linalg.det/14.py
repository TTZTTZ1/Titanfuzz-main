
import torch
n = 4
A = torch.randn(n, n)
result = torch.linalg.det(A)
print(result)
