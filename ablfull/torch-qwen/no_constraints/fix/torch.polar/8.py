import torch
r = torch.tensor([1.0, 2.0])
theta = torch.tensor([0.5, 1.5])
result = torch.polar(r, theta)
print(result)