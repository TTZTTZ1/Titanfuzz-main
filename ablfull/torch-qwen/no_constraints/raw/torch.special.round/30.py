import torch

input_data = torch.tensor([0.5, -0.5, 2.7, -2.7])
result = torch.special.round(input_data)
print(result)