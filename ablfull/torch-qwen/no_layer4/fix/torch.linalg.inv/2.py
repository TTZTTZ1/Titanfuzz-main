import torch
n = 4
A = torch.randn(n, n, dtype=torch.float)
result = torch.linalg.inv(A)