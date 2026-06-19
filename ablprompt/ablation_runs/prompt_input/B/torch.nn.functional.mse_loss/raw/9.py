import torch
import torch.nn.functional as F

# Create random tensors for input and target
input_tensor = torch.randn(3, requires_grad=True)
target_tensor = torch.randn(3)

# Compute MSE loss with reduction='sum'
loss = F.mse_loss(input_tensor, target_tensor, reduction='sum')

print(loss)