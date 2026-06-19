
import torch
n = 4
A = torch.randn(n, n, dtype=torch.float)
inv_A = torch.linalg.inv(A)
