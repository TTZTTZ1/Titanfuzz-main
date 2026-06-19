import torch
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 2, 6])
result = a.ne(b)
print(result)