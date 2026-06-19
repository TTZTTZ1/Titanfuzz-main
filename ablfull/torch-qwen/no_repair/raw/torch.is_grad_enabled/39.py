import torch

input_data = None  # No input required for this API
result = torch.is_grad_enabled()
print(result)