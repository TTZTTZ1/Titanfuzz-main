import torch
tensor = torch.tensor([0, 0, 0], dtype=torch.long)
indices = torch.tensor([0, 2], dtype=torch.long)
values = torch.tensor([99, (- 1)], dtype=torch.long)
tensor.put_(indices, values)
print(tensor)