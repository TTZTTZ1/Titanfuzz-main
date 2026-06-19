import torch
indices = torch.tensor([0, 1, 2])
values = torch.tensor([10, 20, 30], dtype=torch.float32)
self = torch.zeros(5, dtype=torch.float32)
self.put_(indices, values)
print(self)