import torch
r = torch.tensor([1.0])
theta = torch.tensor([0.0])
result = torch.polar(r, theta)
print(result)