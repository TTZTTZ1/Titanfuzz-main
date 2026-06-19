import torch
torch.set_grad_enabled(True)
x = torch.tensor(5.0, requires_grad=True)
result = torch.is_grad_enabled()
print(result)