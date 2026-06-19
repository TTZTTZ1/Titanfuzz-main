import torch
input_data = torch.tensor([1.0, (- float('inf')), 2.5, float('nan')])
result = torch.isfinite(input_data)
print(result)