import torch
A = torch.randn(4, 4, dtype=torch.float64)
result = torch.linalg.det(A)
print(result)