import torch
n = 5
A = torch.randn(n, n, dtype=torch.double)
result = torch.linalg.inv(A)