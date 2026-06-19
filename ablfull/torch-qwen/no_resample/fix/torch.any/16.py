import torch
input_tensor = torch.tensor([[0, 1], [2, 3]])
result = torch.any(input_tensor, dim=1)
print(result)