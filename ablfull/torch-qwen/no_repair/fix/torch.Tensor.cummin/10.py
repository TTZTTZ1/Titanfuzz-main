
import torch
input_tensor = torch.tensor([3, 1, 4, 1, 5, 9, 2, 6], dtype=torch.float32)
result = input_tensor.cummin(dim=0)
print(result)
