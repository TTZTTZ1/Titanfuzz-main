import torch

input_data = False  # Valid boolean value
result = torch.is_grad_enabled(input_data)
print(result)