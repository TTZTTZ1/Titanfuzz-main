import torch
input_data = torch.tensor([1.0, 2.0, float('inf'), (- float('inf')), float('nan')])
result = torch.isfinite(input_data)
print(result)