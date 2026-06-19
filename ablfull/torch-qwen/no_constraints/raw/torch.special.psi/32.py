import torch

input_data = torch.tensor(1.0)
result = torch.special.psi(input_data)
print(result)