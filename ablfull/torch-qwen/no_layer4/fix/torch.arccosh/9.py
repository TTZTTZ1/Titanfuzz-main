import torch
input_tensor = torch.tensor([2.0, 3.0], dtype=torch.float)
result = torch.arccosh(input_tensor)
print(result)