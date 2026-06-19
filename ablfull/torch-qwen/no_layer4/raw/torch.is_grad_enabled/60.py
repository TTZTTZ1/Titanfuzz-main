import torch

# Disable gradient calculation to satisfy the constraint
torch.set_grad_enabled(False)

# Check if gradient calculation is disabled
result = torch.is_grad_enabled()

print(result)