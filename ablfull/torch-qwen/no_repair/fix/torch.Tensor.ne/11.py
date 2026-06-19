
import torch
a = torch.tensor([1, 2, 3], dtype=torch.int)
b = torch.tensor([1, 0, 3], dtype=torch.int)
result = a.ne(b)
print(result)
