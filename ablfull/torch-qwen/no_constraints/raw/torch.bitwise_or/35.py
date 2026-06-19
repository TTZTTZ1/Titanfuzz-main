import torch

x = torch.tensor([1, 0, 1], dtype=torch.uint8)
y = torch.tensor([0, 1, 1], dtype=torch.uint8)
result = torch.bitwise_or(x, y)