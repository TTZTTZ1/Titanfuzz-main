import torch

mean = torch.tensor([0.0])
std = torch.tensor([1.0])
size = (3, 3)

result = torch.normal(mean, std, size)