import torch
data = torch.tensor([1, 2, 3])
indices = torch.tensor([0, 2])
values = torch.tensor([9, 8])
result = data.put_(indices, values)
print(result)