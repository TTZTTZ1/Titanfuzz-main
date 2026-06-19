
import torch
A = torch.randn(3, 3, dtype=torch.float64)
result = torch.linalg.det(A)
