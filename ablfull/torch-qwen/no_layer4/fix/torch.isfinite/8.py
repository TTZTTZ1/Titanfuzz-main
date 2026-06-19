import torch
input_tensor = torch.tensor([1.0, (- float('inf')), 2.0, float('nan')], dtype=torch.float32)
result = torch.isfinite(input_tensor)
print(result)