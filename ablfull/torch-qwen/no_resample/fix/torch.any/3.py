import torch
input_tensor = torch.tensor([[0, 1], [2, 0]])
result = torch.any(input_tensor)
print(result)