import torch

A = torch.randn(2, 2, dtype=torch.float)
check_errors = False
out = None

result = torch.linalg.inv_ex(A, check_errors=check_errors, out=out)