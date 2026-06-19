import torch

# Ensure gradient tracking is enabled for this example
torch.set_grad_enabled(True)

# Check if gradient tracking is enabled
result = torch.is_grad_enabled()

print(result)