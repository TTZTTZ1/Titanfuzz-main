import torch
x = torch.tensor([4.0], dtype=torch.float32)
y = torch.tensor([2.0], dtype=torch.float32)
result = torch.divide(x, y)
print(result)