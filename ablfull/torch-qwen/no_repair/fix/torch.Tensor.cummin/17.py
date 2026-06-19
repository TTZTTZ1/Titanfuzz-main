
import torch
input_tensor = torch.tensor([3, 1, 4, 1, 5, 9])
result = torch.Tensor.cummin(input_tensor, dim=0)
print(result)
