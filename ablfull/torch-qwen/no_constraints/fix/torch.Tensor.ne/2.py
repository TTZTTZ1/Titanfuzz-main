import torch
a = torch.tensor([1, 2, 3])
b = torch.tensor([1, 0, 3])
result = a.ne(b)
print(result)