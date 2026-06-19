import torch
torch.set_grad_enabled(True)
input_tensor = torch.tensor([1.0, 2.0], requires_grad=True)
result = torch.is_grad_enabled()
print(result)