
import torch
a = torch.tensor([[1.0, 2.0, 3.0]])
b = torch.tensor([[4.0, 5.0, 6.0]])
result = torch.Tensor.cross(a, b)
print(result)
