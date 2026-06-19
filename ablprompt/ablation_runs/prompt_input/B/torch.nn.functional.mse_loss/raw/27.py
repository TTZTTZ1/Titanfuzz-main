import torch
import torch.nn.functional as F

# Create some random tensors for input and target
input_tensor = torch.randn(3, requires_grad=True)
target_tensor = torch.randn(3)

# Calculate MSE loss with reduction='mean'
mse_loss = F.mse_loss(input_tensor, target_tensor, reduction='mean')

# Print the computed loss
print("MSE Loss:", mse_loss.item())