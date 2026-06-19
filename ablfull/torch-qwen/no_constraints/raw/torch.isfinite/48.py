import torch

input_data = torch.tensor([float('inf'), -float('inf'), 0.5, float('-nan')])
result = torch.isfinite(input_data)
print(result)