import torch
with torch.no_grad():
    dummy_tensor = torch.tensor([1.0, 2.0], requires_grad=False)
    result = torch.is_grad_enabled()
print(result)