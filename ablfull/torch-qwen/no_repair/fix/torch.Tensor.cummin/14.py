
import torch
input_tensor = torch.tensor([[7, 2, 5], [6, 3, 4]])
result = input_tensor.cummin(dim=1)
print(result)
