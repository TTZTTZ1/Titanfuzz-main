import torch
input_tensor = torch.tensor([2.0, 3.0, 4.0], dtype=torch.float)
output_tensor = torch.arccosh(input_tensor)
print(output_tensor)