import torch
x = torch.tensor([1.0, 2.0, 3.0])
y = 2.5
result = x.ne(y)
print(result)