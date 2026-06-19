import torch
import torch.nn.functional as F

# Create some random tensors for input and target
input = torch.randn(3, requires_grad=True)
target = torch.randn(3)

# Compute MSE loss
loss = F.mse_loss(input, target, reduction='mean')

# Print the loss
print(loss)