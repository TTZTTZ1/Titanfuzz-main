import torch
n = 4
A = torch.randn(n, n)
A = (A @ A.T)
result = torch.linalg.inv(A)
print(result)