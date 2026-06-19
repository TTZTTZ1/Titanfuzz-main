
import torch
n = 5
A = torch.randn(n, n)
inv_A = torch.linalg.inv(A)
