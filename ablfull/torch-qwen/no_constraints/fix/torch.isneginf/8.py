import torch
input_data = torch.tensor([(- float('inf')), (- 1.0), 0.0, float('inf')])
result = torch.isneginf(input_data)