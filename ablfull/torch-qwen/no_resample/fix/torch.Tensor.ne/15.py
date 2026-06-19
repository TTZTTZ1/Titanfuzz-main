import torch
a = torch.tensor([1, 2, 3], dtype=torch.float)
b = 2
result = a.ne(b)
print(result)