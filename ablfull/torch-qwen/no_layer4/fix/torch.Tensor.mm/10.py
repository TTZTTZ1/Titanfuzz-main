import torch
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
b = torch.tensor([[2, 0], [1, 2]], dtype=torch.float)
result = torch.mm(a, b)