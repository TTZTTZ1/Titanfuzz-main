
import torch
a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([1.0, 2.5, 3.0])
result = a.ne(b)
print(result)
