import torch
a = torch.tensor([[1, 2], [3, 4]])
result = torch.transpose(a, 0, 1)
print(result)