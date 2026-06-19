import torch
input_tensor = torch.tensor([[10, 5], [3, 8]])
result = input_tensor.cummin(dim=1)
print(result)