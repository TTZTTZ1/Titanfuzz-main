import torch
x = torch.tensor([1.0], dtype=torch.float32)
y = torch.tensor([0.0], dtype=torch.float32)
result = torch.atan2(y, x)
print(result)