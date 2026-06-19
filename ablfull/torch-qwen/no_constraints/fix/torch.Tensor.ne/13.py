import torch
x = torch.tensor([1, 2, 3], dtype=torch.float32)
y = torch.tensor([1, 0, 3], dtype=torch.float32)
result = x.ne(y)
print(result)