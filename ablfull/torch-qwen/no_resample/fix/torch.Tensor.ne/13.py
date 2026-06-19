import torch
tensor = torch.tensor([1, 2, 3], dtype=torch.int)
other = torch.tensor([1, 0, 3], dtype=torch.int)
result = tensor.ne(other)
print(result)