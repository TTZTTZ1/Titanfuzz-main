
import torch
n = 4
A = torch.randn(n, n, dtype=torch.double)
result = torch.linalg.inv(A)
