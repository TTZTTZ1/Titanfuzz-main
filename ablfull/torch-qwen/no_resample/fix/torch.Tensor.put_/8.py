import torch
index = torch.tensor([0, 1, 2], dtype=torch.long)
source = torch.tensor([3, 4, 5], dtype=torch.float)
result = torch.zeros(3, dtype=torch.float).put_(index, source)