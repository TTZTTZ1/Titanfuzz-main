
import torch
n = 4
A = torch.randn(n, n)
out = None
result = torch.linalg.inv(A, out=out)
