import torch
n = 4
A = torch.randn(n, n)
A_inv = torch.linalg.inv(A)
print(A_inv)