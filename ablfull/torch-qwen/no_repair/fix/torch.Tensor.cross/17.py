
import torch
a = torch.tensor([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
b = torch.tensor([[0.0, 1.0, 0.0], [1.0, 0.0, 0.0]])
result = a.cross(b, dim=1)
print(result)
