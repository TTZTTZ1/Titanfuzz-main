import torch

input_tensor = torch.tensor([0.5, -1.5], dtype=torch.float32)
output_tensor = torch.special.psi(input_tensor)