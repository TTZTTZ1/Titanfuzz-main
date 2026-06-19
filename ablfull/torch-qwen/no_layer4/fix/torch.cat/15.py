import torch
tensors = [torch.randn(3), torch.randn(3)]
dim = 0
result = torch.cat(tensors, dim=dim)