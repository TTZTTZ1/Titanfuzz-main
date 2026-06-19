import torch
a = torch.tensor([1.0, 2.0], dtype=torch.float)
b = torch.tensor([3.0, 4.0], dtype=torch.float)
result = a.add_(b)
print(result)