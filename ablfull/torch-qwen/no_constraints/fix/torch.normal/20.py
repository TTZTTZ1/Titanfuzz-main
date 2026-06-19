import torch
mean = torch.tensor([0.0])
std = torch.tensor([1.0])
input_data = torch.normal(mean=mean, std=std)
print(input_data)