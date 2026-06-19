import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
result = input_tensor.cummin(dim=1)
print(result)