import torch

# Disable gradient calculation
torch.set_grad_enabled(False)

# Check if gradient calculation is enabled
result = torch.is_grad_enabled()
print(result)