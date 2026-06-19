import torch

a = torch.tensor([1, 0, 1], dtype=torch.uint8)
b = torch.tensor([0, 1, 1], dtype=torch.uint8)
result = torch.bitwise_or(a, b)