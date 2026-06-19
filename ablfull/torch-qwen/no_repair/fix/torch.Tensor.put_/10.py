
import torch
index = torch.tensor([0, 1, 2])
source = torch.tensor([9, 8, 7], dtype=torch.int)
accumulate = False
result = torch.zeros(4, dtype=torch.int).put_(index, source, accumulate=accumulate)
print(result)
