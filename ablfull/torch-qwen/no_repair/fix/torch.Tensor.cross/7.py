
import torch
a = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
b = torch.tensor([[7.0, 8.0, 9.0], [10.0, 11.0, 12.0]])
result = a.cross(b, dim=1)
print(result)
