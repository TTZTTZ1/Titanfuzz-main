import torch

input_data = torch.tensor([0.5, 1.5], dtype=torch.float32)
psi_value = torch.special.psi(input_data)
print(psi_value)