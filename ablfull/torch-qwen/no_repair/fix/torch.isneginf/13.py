
import torch
input_tensor = torch.tensor([(- float('inf')), 0.0, float('inf')])
result = torch.isneginf(input_tensor)
