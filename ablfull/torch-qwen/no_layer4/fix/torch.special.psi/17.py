import torch
input_data = torch.tensor([(- 2.0), (- 1.5), (- 0.5), 0.0, 0.5, 1.0, 2.0])
output = torch.special.psi(input_data)