import torch
tensor = torch.tensor([0, 1, 2, 3])
indices = torch.tensor([0, 2])
values = torch.tensor([9, 8])
tensor.put_(indices, values)
print(tensor)