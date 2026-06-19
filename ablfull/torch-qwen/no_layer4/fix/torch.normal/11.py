import torch
mean = torch.tensor([0.5])
std = torch.tensor([0.5])
output = torch.normal(mean=mean, std=std)