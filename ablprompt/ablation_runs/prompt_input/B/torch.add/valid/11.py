import torch

a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
b = torch.tensor([[0.5, -0.5], [-1, 1]], dtype=torch.float)
alpha = 2
result = torch.add(a, b, alpha=alpha)
print(result)