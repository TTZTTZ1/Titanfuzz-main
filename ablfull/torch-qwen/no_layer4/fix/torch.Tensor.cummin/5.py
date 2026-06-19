import torch
input_tensor = torch.tensor([1, 3, 2])
result = input_tensor.cummin(dim=0)
print(result)