import torch
A = torch.tensor([[4.0, 7.0], [2.0, 6.0]])
det = torch.linalg.det(A)
print(det)