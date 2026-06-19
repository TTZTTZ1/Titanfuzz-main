
import torch
A = torch.randn(4, 4)
result = torch.linalg.inv_ex(A, check_errors=True)
