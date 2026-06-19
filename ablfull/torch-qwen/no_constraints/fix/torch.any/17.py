import torch
x = torch.tensor([[0, 0], [0, 1]])
result = torch.any(x)
print(result)