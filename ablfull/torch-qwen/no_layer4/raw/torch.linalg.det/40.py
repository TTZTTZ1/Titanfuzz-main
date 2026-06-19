import torch

A = torch.randn(3, 3)
det_A = torch.linalg.det(A)
print(det_A)