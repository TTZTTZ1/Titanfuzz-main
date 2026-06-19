import torch

input_tensor = torch.tensor([0.5, 1.0, 1.5], dtype=torch.float32)
result = torch.special.psi(input_tensor)