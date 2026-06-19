
import torch
a = torch.tensor([[1, 0, 0], [0, 1, 0]])
b = torch.tensor([[0, 0, 1], [1, 0, 0]])
result = torch.Tensor.cross(a, b)
