import torch

# Ensure gradient calculation is enabled
torch.set_grad_enabled(True)

# Check if gradient calculation is enabled
result = torch.is_grad_enabled()
print(result)