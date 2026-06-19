import torch

input_data = torch.tensor([-1.0, -0.5, 0.0, 0.5, 1.0], dtype=torch.float32)
result = torch.special.psi(input_data)
print(result)