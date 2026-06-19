import torch
indices = torch.tensor([0, 2], dtype=torch.long)
values = torch.tensor([99, (- 99)], dtype=torch.float)
tensor = torch.zeros(5, dtype=torch.float)
tensor.put_(indices, values)
print(tensor)