
import torch
n = 4
A = torch.randn(n, n)
A[(0, 0)] += (abs(A.min()) + 1)
result = torch.linalg.inv(A)
