
import torch
x = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float)
y = torch.tensor([1.0, 2.5, 3.0])
result = x.ne(y)
print(result)
