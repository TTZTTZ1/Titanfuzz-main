import torch
import torch.nn.functional as F

# Example tensors
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
target_tensor = torch.tensor([[1.5, 2.5], [3.5, 4.5]])

# Compute MSE loss with reduction='mean'
mse_loss = F.mse_loss(input_tensor, target_tensor, reduction='mean')
print("Mean Squared Error Loss:", mse_loss.item())

# Compute MSE loss with reduction='sum'
mse_loss_sum = F.mse_loss(input_tensor, target_tensor, reduction='sum')
print("Sum of Squared Errors:", mse_loss_sum.item())

# Compute MSE loss with custom weights
weights = torch.tensor([0.5, 1.0])
weighted_mse_loss = F.mse_loss(input_tensor, target_tensor, weight=weights, reduction='mean')
print("Weighted Mean Squared Error Loss:", weighted_mse_loss.item())