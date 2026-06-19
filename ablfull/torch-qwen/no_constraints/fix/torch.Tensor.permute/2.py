import torch
data = torch.randn(2, 3, 4)
result = data.permute(2, 0, 1)