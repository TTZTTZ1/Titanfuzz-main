import torch
n = 5
A = torch.randn(n, n, dtype=torch.float64)
result = torch.linalg.inv(A)