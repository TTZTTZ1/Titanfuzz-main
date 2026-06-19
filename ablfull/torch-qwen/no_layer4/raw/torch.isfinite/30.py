import torch

input_tensor = torch.tensor([1.0, 2.0, float('inf'), -float('inf'), float('nan')], dtype=torch.float32)
result = torch.isfinite(input_tensor)
print(result)