
import torch
A = torch.randn(4, 4, dtype=torch.float)
result = torch.linalg.det(A)
