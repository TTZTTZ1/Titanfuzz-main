import torch
index = torch.tensor([0, 1, 2])
source = torch.tensor([10, 20, 30])
result = torch.tensor([5, 6, 7]).put_(index, source)
print(result)