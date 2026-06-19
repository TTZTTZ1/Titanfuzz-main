import torch

a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
b = torch.tensor([[0.5, -1.0], [2.0, -0.5]], dtype=torch.float32)
c = torch.tensor(2.0, dtype=torch.float32)

result = torch.add(a, b, alpha=c)
print(result)