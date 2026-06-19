
import torch
tensors = [torch.tensor([1, 2, 3]), torch.tensor([4, 5])]
dim = 0
result = torch.cat(tensors, dim)
