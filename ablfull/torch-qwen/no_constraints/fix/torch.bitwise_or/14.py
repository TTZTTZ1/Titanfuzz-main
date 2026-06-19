import torch
a = torch.tensor([1, 0, 3], dtype=torch.int64)
b = torch.tensor([4, 5, 6], dtype=torch.int64)
result = torch.bitwise_or(a, b)
print(result)