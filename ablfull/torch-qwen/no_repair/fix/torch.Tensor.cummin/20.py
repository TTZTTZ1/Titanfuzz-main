
import torch
input_tensor = torch.tensor([3, 1, 4, 1, 5, 9])
dim = 0
result = input_tensor.cummin(dim)
print(result)
