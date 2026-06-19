import torch
mean = torch.tensor([0.5])
std = torch.tensor([1.0])
result = torch.normal(mean=mean, std=std)