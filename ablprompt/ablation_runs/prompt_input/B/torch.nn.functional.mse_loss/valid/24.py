import torch
import torch.nn.functional as F

# Create some random tensors for demonstration
input_tensor = torch.randn(3, requires_grad=True)
target_tensor = torch.randn(3)

# Compute the MSE loss
loss = F.mse_loss(input_tensor, target_tensor, reduction='mean')

print(loss)