import torch
input_tensor = torch.tensor([[7, 2], [5, 6]])
result = input_tensor.cummin(dim=0)
print(result)