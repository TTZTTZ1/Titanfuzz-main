import torch
input_data = torch.tensor([2.0, 3.0, 4.5], dtype=torch.float)
result = torch.arccosh(input_data)
print(result)