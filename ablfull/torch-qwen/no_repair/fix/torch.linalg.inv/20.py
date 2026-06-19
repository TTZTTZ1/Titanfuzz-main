
import torch
n = 4
A = torch.randn(n, n)
inv_A = torch.linalg.inv(A)
result = torch.linalg.inv(A, out=inv_A)
