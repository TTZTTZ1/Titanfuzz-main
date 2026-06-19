import torch

mean = torch.tensor([0.5])
std = torch.tensor([0.5])

result = torch.normal(mean=mean, std=std)