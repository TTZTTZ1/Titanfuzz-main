import torch
index = torch.tensor([0, 2])
source = torch.tensor([5, 9], dtype=torch.float)
accumulate = False
result = torch.zeros(4)
result.put_(index, source, accumulate)
print(result)