import torch
a = torch.tensor([1, 2, 3], dtype=torch.uint8)
b = torch.tensor([4, 5, 6], dtype=torch.uint8)
result = torch.bitwise_or(a, b)
print(result)