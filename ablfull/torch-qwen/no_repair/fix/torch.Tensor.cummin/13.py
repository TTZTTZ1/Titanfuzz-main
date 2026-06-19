
import torch
input_tensor = torch.tensor([[1, 2], [0, 4]])
result = input_tensor.cummin(dim=1)
print(result)
