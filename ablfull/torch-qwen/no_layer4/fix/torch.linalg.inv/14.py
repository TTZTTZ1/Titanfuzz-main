import torch
n = 3
A = torch.randn(n, n)
inv_A = torch.linalg.inv(A)