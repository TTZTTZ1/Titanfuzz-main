import torch
from torch.nn.functional import mse_loss

# Create some example data
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]], requires_grad=True)
target_tensor = torch.tensor([[1.5, 2.5], [3.5, 4.5]])

# Compute the MSE loss
loss = mse_loss(input_tensor, target_tensor, reduction='mean')

print(f"MSE Loss: {loss.item()}")