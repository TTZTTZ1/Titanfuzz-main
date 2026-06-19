
import torch
n = 4
A = torch.randn(n, n)
A = ((A @ A.t()) + (torch.eye(n) * 0.5))
result = torch.linalg.inv(A)
