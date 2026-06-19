
import torch
n = 4
A = torch.randn(n, n)
A_inv = torch.linalg.inv(A)
result = torch.linalg.inv(A, out=A_inv)
