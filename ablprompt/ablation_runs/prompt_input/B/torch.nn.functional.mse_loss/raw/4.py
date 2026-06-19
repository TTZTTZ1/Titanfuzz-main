import torch
import torch.nn.functional as F

# Create random tensors for input and target
input_tensor = torch.randn(3, 4)
target_tensor = torch.randn(3, 4)

# Compute MSE loss
loss = F.mse_loss(input_tensor, target_tensor, reduction='mean')

print(loss)