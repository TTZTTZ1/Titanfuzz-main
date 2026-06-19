import torch
x = torch.tensor([1.0, 2.0], dtype=torch.float32)
y = torch.tensor([3.0, 4.0], dtype=torch.float32)
x.add_(y)