
import torch
input_tensor = torch.tensor([[10, 50], [30, 20]])
result = input_tensor.cummin(dim=1)
print(result)
