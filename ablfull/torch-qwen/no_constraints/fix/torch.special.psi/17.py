import torch
x = torch.tensor(0.5, requires_grad=True)
result = torch.special.psi(x)
print(result)