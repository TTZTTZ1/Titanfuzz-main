import torch

input_data = torch.tensor([0.5, -0.3, 1.2], dtype=torch.float32)
result = torch.special.psi(input_data)