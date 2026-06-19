import torch
indices = torch.tensor([0, 1, 2], dtype=torch.long)
values = torch.tensor([10, 20, 30], dtype=torch.float)
tensor = torch.zeros(5, dtype=torch.float)
tensor.put_(indices, values)
print(tensor)