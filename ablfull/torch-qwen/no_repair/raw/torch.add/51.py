import torch

x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
y = torch.tensor([5], dtype=torch.float)

result = torch.add(x, y)
print(result)