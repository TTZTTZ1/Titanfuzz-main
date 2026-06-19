
import torch
tensors = [torch.tensor([]), torch.tensor([1, 2]), torch.tensor([3, 4])]
dim = 0
result = torch.cat(tensors, dim=dim)
print(result)
