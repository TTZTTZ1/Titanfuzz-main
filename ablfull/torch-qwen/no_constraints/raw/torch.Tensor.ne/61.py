import torch

x = torch.tensor([1, 2, 3])
y = torch.tensor([1, 0, 3])
result = x.ne(y)
print(result)