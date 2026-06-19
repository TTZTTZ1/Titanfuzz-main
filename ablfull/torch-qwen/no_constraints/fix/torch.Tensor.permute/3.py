import torch
data = torch.randn(3, 4)
permuted_data = data.permute(1, 0)