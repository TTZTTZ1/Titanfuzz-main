
import torch
A = torch.randn(3, 3, dtype=torch.double)
result = torch.linalg.inv_ex(A)
