
import torch
n = 3
A = torch.randn(n, n, dtype=torch.float)
result = torch.linalg.inv(A)
