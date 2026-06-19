
import torch
a = torch.tensor([(- 1.0), (- 2.0)], dtype=torch.float32)
b = torch.tensor([1.0, 2.0], dtype=torch.float32)
result = a.copysign_(b)
print(result)
