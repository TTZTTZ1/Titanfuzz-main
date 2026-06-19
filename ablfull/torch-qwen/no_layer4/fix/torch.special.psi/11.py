import torch
input_data = torch.tensor([(- 2.0), (- 1.5), 0.0, 1.0], dtype=torch.float32)
result = torch.special.psi(input_data)
print(result)