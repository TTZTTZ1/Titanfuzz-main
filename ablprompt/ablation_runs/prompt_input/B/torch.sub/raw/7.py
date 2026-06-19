import torch

a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
b = torch.tensor([[0.5, 1.5], [2.5, 3.5]], dtype=torch.float32)
alpha = 2
result = torch.sub(a, b, alpha=alpha)
print(result)