import torch

input_tensor = torch.tensor([-float('inf'), 0.5, float('inf')])
result = torch.isneginf(input_tensor)
print(result)