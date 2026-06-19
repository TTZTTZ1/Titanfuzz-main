
import torch
tensors = [torch.randn(0), torch.randn(5)]
dim = 0
result = torch.cat(tensors, dim)
