import torch
input_data = torch.tensor([2.0, 5.0, 7.0], dtype=torch.float)
result = torch.arccosh(input_data)
print(result)