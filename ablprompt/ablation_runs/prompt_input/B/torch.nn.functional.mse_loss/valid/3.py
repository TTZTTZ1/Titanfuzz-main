import torch
import torch.nn.functional as F

# Create random input and target tensors
input_tensor = torch.randn(3, requires_grad=True)
target_tensor = torch.randn(3)

# Compute MSE loss
loss = F.mse_loss(input_tensor, target_tensor, reduction='mean')

# Print the computed loss
print(loss)