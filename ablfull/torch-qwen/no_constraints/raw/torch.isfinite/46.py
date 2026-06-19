import torch

input_data = torch.tensor([0.5, -float('inf'), float('nan'), 1.0])
result = torch.isfinite(input_data)
print(result)