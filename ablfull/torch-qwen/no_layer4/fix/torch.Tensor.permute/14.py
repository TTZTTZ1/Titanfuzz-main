import torch
data = torch.randn(2, 3, 4)
permuted_data = data.permute(2, 0, 1)