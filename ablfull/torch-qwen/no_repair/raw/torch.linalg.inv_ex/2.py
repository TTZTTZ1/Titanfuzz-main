import torch

A = torch.randn(3, 3)
result = torch.linalg.inv_ex(A, check_errors=True)