import torch

input_data = False  # Satisfies the constraint for bool type
result = torch.is_grad_enabled(input_data)
print(result)