import torch
index = torch.tensor([0, 1, 2], dtype=torch.long)
source = torch.tensor([9, 8, 7], dtype=torch.float)
result = torch.zeros(5, dtype=torch.float)
result.put_(index, source)
print(result)