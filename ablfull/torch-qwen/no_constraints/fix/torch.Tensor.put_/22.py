import torch
indices = torch.tensor([0, 1, 2])
values = torch.tensor([3.0, 4.0, 5.0])
tensor = torch.zeros(3)
tensor.put_(indices, values)
print(tensor)