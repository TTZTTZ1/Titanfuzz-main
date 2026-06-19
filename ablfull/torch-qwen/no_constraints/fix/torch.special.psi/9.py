import torch
x = torch.tensor([(- 4.0), 0.0], dtype=torch.float32)
result = torch.special.psi(x)
print(result)