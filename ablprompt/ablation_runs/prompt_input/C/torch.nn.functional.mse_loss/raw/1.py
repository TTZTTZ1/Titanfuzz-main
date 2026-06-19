import torch
import torch.nn.functional as F

# Create some random tensors for demonstration
input_tensor = torch.randn(3, requires_grad=True)
target_tensor = torch.randn(3)

# Calculate MSE loss without any weighting or reduction
loss = F.mse_loss(input_tensor, target_tensor, reduction='none')
print("Loss without reduction:", loss)

# Calculate MSE loss with mean reduction
loss_mean = F.mse_loss(input_tensor, target_tensor, reduction='mean')
print("Mean Loss:", loss_mean)

# Calculate MSE loss with sum reduction
loss_sum = F.mse_loss(input_tensor, target_tensor, reduction='sum')
print("Sum Loss:", loss_sum)

# Calculate MSE loss with custom weights
weights = torch.tensor([0.5, 1.0, 1.5])
weighted_loss = F.mse_loss(input_tensor, target_tensor, weight=weights, reduction='mean')
print("Weighted Mean Loss:", weighted_loss)