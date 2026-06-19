
import torch
index = torch.tensor([0, 1])
source = torch.tensor([3, 4])
result = torch.tensor([1, 2]).put_(index, source)
print(result)
