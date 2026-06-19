import torch
indices = torch.tensor([0, 1, 2])
values = torch.tensor([10, 20, 30], dtype=torch.float32)
tensor = torch.zeros(5)
tensor.put_(indices, values)
print(tensor)