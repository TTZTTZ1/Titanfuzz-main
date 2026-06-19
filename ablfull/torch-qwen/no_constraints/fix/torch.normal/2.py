import torch
mean = torch.tensor([0.0])
std_dev = torch.tensor([1.0])
result = torch.normal(mean, std_dev)
print(result)