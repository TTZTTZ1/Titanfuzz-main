import torch
input_data = torch.tensor([1.0], requires_grad=True)
output = torch.is_grad_enabled()
print(output)