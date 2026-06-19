import torch

# Disable gradient tracking
torch.set_grad_enabled(False)

# Check if gradient tracking is enabled
result = torch.is_grad_enabled()

print(result)