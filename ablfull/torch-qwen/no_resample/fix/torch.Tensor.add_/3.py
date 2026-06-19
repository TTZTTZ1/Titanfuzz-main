import torch
a = torch.tensor([1.0, 2.0])
other = torch.tensor([3.0, 4.0])
result = a.add_(other)
print(result)