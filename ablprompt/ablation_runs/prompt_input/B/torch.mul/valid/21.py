import torch

a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
b = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)
c = torch.zeros_like(a)

result = torch.mul(a, b, out=c)
print(result)