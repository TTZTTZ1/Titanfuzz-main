import torch

input_data = torch.tensor([0.5, -0.5, 1.4, -1.6], dtype=torch.float32)
result = torch.special.round(input_data)
print(result)