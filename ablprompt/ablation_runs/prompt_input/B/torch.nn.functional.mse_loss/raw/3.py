import torch
from torch.nn.functional import mse_loss

# Create some random tensors for demonstration
input_tensor = torch.randn(3, requires_grad=True)
target_tensor = torch.randn(3)

# Compute MSE loss without any additional parameters
loss = mse_loss(input_tensor, target_tensor)

print("MSE Loss:", loss.item())