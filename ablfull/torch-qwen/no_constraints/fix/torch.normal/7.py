import torch
mean = torch.tensor(0.0)
std = torch.tensor(1.0)
output = torch.normal(mean, std, size=(3,))
print(output)