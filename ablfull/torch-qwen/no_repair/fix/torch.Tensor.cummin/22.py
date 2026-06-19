
import torch
input_data = torch.tensor([[1, 4, 3], [8, 5, 6]])
result = input_data.cummin(dim=1)
print(result)
