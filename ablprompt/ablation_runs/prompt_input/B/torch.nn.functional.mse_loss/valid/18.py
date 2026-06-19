import torch
from torch.nn.functional import mse_loss

# Create some random tensors for input and target
input_tensor = torch.randn(3, requires_grad=True)
target_tensor = torch.randn(3)

# Compute MSE loss
loss = mse_loss(input_tensor, target_tensor, reduction='mean')

print(f"MSE Loss: {loss.item()}")