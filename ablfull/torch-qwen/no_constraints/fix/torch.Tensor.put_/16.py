import torch
tensor = torch.tensor([1, 2, 3], dtype=torch.long)
indices = torch.tensor([0, 2], dtype=torch.long)
values = torch.tensor([4, 5], dtype=torch.long)
tensor.put_(indices, values)
print(tensor)