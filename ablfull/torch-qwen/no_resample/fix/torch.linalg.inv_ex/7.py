import torch
A = torch.randn(2, 2, dtype=torch.float)
result = torch.linalg.inv_ex(A)