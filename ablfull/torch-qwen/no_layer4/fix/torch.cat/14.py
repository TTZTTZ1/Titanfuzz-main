import torch
tensors = [torch.randn(5), torch.randn(5)]
dim = 0
result = torch.cat(tensors, dim=dim)