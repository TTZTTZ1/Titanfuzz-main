import torch
input_data = torch.tensor([0.5, 1.5, 2.5], dtype=torch.float32)
result = torch.special.psi(input_data)
print(result)