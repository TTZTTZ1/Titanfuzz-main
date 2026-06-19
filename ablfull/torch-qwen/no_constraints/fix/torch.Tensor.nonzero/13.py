import torch
data = torch.tensor([[0, 1, 2], [3, 0, 5], [6, 7, 0]])
result = data.nonzero()
print(result)