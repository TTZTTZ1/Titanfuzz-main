import torch

A = torch.randn(2, 2, dtype=torch.double)
result = torch.linalg.inv_ex(A)