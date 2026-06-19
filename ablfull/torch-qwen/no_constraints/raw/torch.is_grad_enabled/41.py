import torch

# Ensure gradients are enabled
torch.set_grad_enabled(True)

# Check if gradients are enabled
result = torch.is_grad_enabled()

print(result)