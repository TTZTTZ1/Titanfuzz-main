import torch
tensor = torch.tensor([1.0, 2.0, 3.0])
other = torch.tensor([1.0, 2.5, 3.0])
result = tensor.ne(other)
print(result)