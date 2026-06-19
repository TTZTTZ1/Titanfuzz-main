import torch
tensor = torch.tensor([1.0, 2.0, 3.0])
other = 2.5
result = tensor.ne(other)
print(result)