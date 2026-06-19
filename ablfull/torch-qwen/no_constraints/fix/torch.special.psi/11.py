import torch
input_data = torch.tensor(0.5)
result = torch.special.psi(input_data)
print(result)