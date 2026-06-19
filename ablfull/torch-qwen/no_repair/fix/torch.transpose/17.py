
import torch
x = torch.tensor([[1, 2], [3, 4]])
result = torch.transpose(x, 0, 1)
print(result)
