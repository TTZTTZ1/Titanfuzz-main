import torch
indices = torch.tensor([0, 1, 2])
values = torch.tensor([4, 5, 6], dtype=torch.float32)
tensor = torch.zeros(3)
tensor.put_(indices, values)
print(tensor)