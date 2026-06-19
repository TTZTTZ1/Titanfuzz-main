import torch

# Ensure gradient calculation is enabled
torch.set_grad_enabled(True)

# Create a tensor with requires_grad=True to trigger gradient computation
x = torch.tensor(5.0, requires_grad=True)

# Check if gradient calculation is enabled
result = torch.is_grad_enabled()
print(result)