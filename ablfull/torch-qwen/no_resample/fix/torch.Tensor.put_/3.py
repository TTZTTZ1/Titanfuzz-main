import torch
index = torch.tensor([0, 1, 2], dtype=torch.long)
source = torch.tensor([4, 5, 6], dtype=torch.float)
result = torch.zeros(3, dtype=torch.float)
result.put_(index, source)
print(result)