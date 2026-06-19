
import torch
input_tensor = torch.tensor([(- float('inf')), 0.5, float('nan')])
result = torch.isneginf(input_tensor)
print(result)
