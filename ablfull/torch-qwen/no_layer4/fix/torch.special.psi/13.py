import torch
input_data = torch.tensor([(- 0.5), (- 0.3), 0.0, 0.7], dtype=torch.float32)
output = torch.special.psi(input_data)