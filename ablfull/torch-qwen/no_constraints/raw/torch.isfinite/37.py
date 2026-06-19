import torch

input_data = torch.tensor([0.0, float('inf'), -float('inf'), float('nan')])
result = torch.isfinite(input_data)
print(result)