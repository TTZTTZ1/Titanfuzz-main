import torch
a = torch.tensor([[1, 0, 0], [0, 1, 0]], dtype=torch.float32)
b = torch.tensor([[0, 0, 1], [1, 0, 0]], dtype=torch.float32)
result = torch.Tensor.cross(a, b, dim=1)
print(result)