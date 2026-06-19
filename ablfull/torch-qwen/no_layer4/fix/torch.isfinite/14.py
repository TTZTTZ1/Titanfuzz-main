import torch
input_tensor = torch.tensor([0.5, float('inf'), (- float('inf')), float('nan')], dtype=torch.float32)
result = torch.isfinite(input_tensor)
print(result)