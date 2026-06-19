import torch
input_tensor = torch.tensor([(- float('inf')), float('nan')])
result = torch.isneginf(input_tensor)
print(result)