import torch
data = torch.randn(2, 3, 4)
dims = (2, 0, 1)
result = data.permute(*dims)