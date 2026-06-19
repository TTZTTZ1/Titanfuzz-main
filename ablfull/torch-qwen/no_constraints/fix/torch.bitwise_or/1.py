import torch
a = torch.tensor([1, 2, 3], dtype=torch.int32)
b = torch.tensor([4, 5, 6], dtype=torch.int32)
result = torch.bitwise_or(a, b)
print(result)