import torch
x = torch.tensor([0.5])
y = torch.tensor([0.5])
result = torch.atan2(y, x)
print(result)