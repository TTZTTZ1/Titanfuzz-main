import torch
data = torch.tensor([[1, 2], [3, 4]])
result = torch.transpose(data, 0, 1)
print(result)