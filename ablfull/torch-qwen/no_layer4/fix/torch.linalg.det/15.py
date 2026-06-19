import torch
A = torch.randn(2, 3, 3, dtype=torch.float)
result = torch.linalg.det(A)