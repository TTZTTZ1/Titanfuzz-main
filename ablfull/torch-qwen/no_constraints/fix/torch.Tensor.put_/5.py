import torch
tensor = torch.tensor([0, 0, 0], dtype=torch.int)
indices = torch.tensor([0, 2])
values = torch.tensor([99, (- 99)], dtype=torch.int)
tensor.put_(indices, values)
print(tensor)