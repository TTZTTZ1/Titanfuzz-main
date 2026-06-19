
import torch
n = 4
A = torch.randn(n, n)
A = ((A @ A.t()) + (n * torch.eye(n)))
inv_A = torch.linalg.inv(A)
