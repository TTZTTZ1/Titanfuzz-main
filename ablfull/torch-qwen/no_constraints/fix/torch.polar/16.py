import torch
r = torch.tensor([1.0], dtype=torch.float32)
theta = torch.tensor([0.5], dtype=torch.float32)
result = torch.polar(r, theta)
print(result)