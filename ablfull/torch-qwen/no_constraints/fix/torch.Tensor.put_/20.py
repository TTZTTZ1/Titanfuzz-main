import torch
indices = torch.tensor([0, 1, 2])
values = torch.tensor([9, 8, 7], dtype=torch.float32)
self_tensor = torch.zeros(3, dtype=torch.float32)
self_tensor.put_(indices, values)