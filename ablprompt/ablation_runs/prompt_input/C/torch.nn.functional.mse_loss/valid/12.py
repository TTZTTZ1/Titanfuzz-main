import torch
import torch.nn.functional as F

# Create some random tensors for input and target
input_tensor = torch.randn(3, 5)
target_tensor = torch.randn(3, 5)

# Compute the MSE loss
mse_loss = F.mse_loss(input_tensor, target_tensor, reduction='mean')

print(f"MSE Loss: {mse_loss.item()}")