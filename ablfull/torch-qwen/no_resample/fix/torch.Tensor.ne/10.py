import torch
tensor = torch.tensor([1, 2, 3], dtype=torch.float)
other = torch.tensor([1, 0, 3], dtype=torch.float)
result = tensor.ne(other)
print(result)