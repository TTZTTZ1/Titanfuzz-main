import torch
input_tensor = torch.tensor([0.5, (- float('inf')), float('nan'), 1.0])
result = torch.isfinite(input_tensor)
print(result)