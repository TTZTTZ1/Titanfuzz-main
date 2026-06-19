import torch

input_data = torch.tensor([-float('inf'), 0., float('inf')])
result = torch.isneginf(input_data)
print(result)