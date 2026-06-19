
import torch
input_data = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
result = torch.is_grad_enabled()
print(result)
