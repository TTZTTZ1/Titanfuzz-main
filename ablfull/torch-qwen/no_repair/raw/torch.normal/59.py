import torch

mean = torch.tensor([0.5, 1.0])
std = torch.tensor([1.0, 1.5])

result = torch.normal(mean=mean, std=std)