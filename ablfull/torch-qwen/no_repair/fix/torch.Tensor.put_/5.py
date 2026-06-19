
import torch
index = torch.tensor([0, 1, 2])
source = torch.tensor([3, 4, 5])
result = torch.tensor([7, 8, 9]).put_(index, source)
print(result)
