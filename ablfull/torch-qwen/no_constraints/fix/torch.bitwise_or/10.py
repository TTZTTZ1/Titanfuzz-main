import torch
a = torch.tensor([1, 0, 3], dtype=torch.uint8)
b = torch.tensor([3, 0, 0], dtype=torch.uint8)
result = torch.bitwise_or(a, b)
print(result)