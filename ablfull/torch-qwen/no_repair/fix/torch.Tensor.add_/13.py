
import torch
a = torch.tensor([1.0, 2.0], dtype=torch.float)
other = torch.tensor([3.0, 4.0], dtype=torch.float)
result = a.add_(other, alpha=2)
print(result)
