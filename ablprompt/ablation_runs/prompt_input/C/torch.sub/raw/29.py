import torch

a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[0, 1], [2, 3]])
result = torch.sub(a, b, alpha=2)
print(result)