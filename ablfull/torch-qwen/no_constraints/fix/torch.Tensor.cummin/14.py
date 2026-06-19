import torch
input_tensor = torch.tensor([[4, 2], [1, 3]])
result = input_tensor.cummin(dim=0)
print(result)