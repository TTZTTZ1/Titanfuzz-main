import torch
from torch.nn.functional import mse_loss

# Create random tensors for input and target
input_tensor = torch.randn(3, requires_grad=True)
target_tensor = torch.randn(3)

# Compute MSE loss with 'mean' reduction
loss = mse_loss(input_tensor, target_tensor)

print(f"Computed MSE Loss: {loss.item()}")