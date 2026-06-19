import torch
n = 3
A = torch.tensor([[4, 7], [2, 6]], dtype=torch.float)
result = torch.linalg.inv(A)