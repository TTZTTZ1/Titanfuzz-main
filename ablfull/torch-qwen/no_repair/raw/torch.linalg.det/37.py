import torch

A = torch.tensor([[4.0, 7.0], [2.0, 6.0]], dtype=torch.float)
det_A = torch.linalg.det(A)