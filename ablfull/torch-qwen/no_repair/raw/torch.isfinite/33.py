import torch

input_tensor = torch.tensor([1.0, 2.0, float('inf'), -float('inf')])
result = torch.isfinite(input_tensor)
print(result)