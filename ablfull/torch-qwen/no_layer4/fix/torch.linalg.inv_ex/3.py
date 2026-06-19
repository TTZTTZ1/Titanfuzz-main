import torch
A = torch.randn(3, 3, dtype=torch.float)
result = torch.linalg.inv_ex(A)