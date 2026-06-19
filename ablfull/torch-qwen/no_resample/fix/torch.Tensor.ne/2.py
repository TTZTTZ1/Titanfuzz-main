import torch
tensor = torch.tensor([1, 2, 3])
other = torch.tensor([1, 0, 3])
result = tensor.ne(other)
print(result)