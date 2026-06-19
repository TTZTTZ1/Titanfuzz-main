import torch
import torch.nn.functional as F

# Create some sample data
input = torch.randn(3, 5, requires_grad=True)
target = torch.randn(3, 5)

# Calculate Mean Squared Error loss
loss = F.mse_loss(input, target)

print('Loss:', loss.item())