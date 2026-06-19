import torch

# Enable gradient calculation
torch.set_grad_enabled(True)

# Check if gradient calculation is enabled
result = torch.is_grad_enabled()

print(result)