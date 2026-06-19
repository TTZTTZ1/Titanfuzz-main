import torch
from torch.nn.functional import mse_loss

# Create random input and target tensors
input_tensor = torch.randn(3, requires_grad=True)
target_tensor = torch.randn(3)

# Compute MSE loss with custom reduction and weighting
weight_tensor = torch.tensor([0.5, 1.0, 1.5])
loss = mse_loss(input_tensor, target_tensor, weight=weight_tensor, reduction='sum')

print(f"Loss: {loss}")