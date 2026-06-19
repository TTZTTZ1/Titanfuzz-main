import torch

a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
b = torch.tensor([0.5, -0.5], dtype=torch.float)
result = torch.add(a, b, alpha=2)
print(result)