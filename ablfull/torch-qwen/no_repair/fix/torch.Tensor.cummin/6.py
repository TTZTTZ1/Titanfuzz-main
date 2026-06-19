
import torch
input_tensor = torch.tensor([[1, 2], [3, 4]])
dim = 0
result = input_tensor.cummin(dim)
print(result)
