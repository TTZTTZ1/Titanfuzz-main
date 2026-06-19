import torch
import torch.nn.functional as F

# Create some random tensors for demonstration
input_tensor = torch.randn(3, 5)
target_tensor = torch.randn(3, 5)

# Compute MSE loss with reduction='sum'
mse_loss = F.mse_loss(input_tensor, target_tensor, reduction='sum')

print("MSE Loss:", mse_loss.item())