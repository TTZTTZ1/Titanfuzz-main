import torch
x = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)
y = torch.tensor([4.0, 5.0, 6.0], dtype=torch.float32)
result = torch.add(x, y)
print(result)