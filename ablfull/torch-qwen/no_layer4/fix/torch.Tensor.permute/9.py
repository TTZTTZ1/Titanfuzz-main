import torch
data = torch.randn(2, 3, 4)
result = data.permute(1, 0, 2)