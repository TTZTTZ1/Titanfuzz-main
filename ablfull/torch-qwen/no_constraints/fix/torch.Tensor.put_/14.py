import torch
tensor = torch.tensor([1, 2, 3])
indices = torch.tensor([0, 2])
values = torch.tensor([4, 5])
tensor.put_(indices, values)
print(tensor)