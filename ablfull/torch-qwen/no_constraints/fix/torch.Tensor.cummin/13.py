import torch
input_tensor = torch.tensor([[1, 2], [3, 4]], dtype=torch.int)
result = input_tensor.cummin(dim=0)
print(result)