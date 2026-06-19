import torch

input_data = True  # This satisfies the constraint for enabling gradient calculation

result = torch.is_grad_enabled(input_data)
print(result)