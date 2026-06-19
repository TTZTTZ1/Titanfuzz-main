import torch

mean = torch.tensor([0.5])
std = torch.tensor([0.5])

# Calling the API with valid tensor inputs
result = torch.normal(mean=mean, std=std)