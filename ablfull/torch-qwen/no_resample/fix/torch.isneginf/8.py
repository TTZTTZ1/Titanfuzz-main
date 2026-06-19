import torch
input_tensor = torch.tensor([(- float('inf')), (- 1.0), 0.0, 1.0])
result = torch.isneginf(input_tensor)
print(result)