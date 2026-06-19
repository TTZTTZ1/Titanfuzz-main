import torch
a = torch.tensor([1, 2, 3], dtype=torch.int)
b = torch.tensor([4, 5, 6], dtype=torch.int)
result = torch.bitwise_or(a, b)
print(result)