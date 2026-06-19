import torch
input_tensor = torch.tensor([[0, 0], [0, 1]])
result = torch.any(input_tensor)
print(result)