import torch
input_tensor = torch.tensor([[1, 2], [0, (- 1)]])
result = input_tensor.cummin(dim=1)
print(result)