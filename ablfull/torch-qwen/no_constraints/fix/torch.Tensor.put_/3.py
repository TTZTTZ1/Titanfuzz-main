import torch
tensor = torch.tensor([0.0, 1.0, 2.0, 3.0])
indices = torch.tensor([0, 2])
values = torch.tensor([99.0, 88.0])
tensor.put_(indices, values)
print(tensor)