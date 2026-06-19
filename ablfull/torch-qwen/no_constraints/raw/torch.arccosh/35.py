import torch

input_data = torch.tensor([2.0], dtype=torch.float32)
result = torch.arccosh(input_data)
print(result)