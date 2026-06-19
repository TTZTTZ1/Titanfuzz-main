import torch
import torch.nn.functional as F

# Create some example data
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
target_tensor = torch.tensor([[1.5, 2.5], [3.5, 4.5]])

# Compute the MSE loss
mse_loss = F.mse_loss(input_tensor, target_tensor, reduction='mean')

print(f"Mean Squared Error Loss: {mse_loss.item()}")