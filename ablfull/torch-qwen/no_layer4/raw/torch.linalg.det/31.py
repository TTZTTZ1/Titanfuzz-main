import torch

A = torch.tensor([[4., 7.], [2., 6.]])
det = torch.linalg.det(A)
print(det)