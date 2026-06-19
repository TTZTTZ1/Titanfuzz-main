import torch
import torch.nn.functional as F

# Create some dummy tensors for demonstration purposes
input = torch.randn(3, 5)
target = torch.randn(3, 5)

# Calculate Mean Squared Error Loss
loss = F.mse_loss(input, target)

print(f"Mean Squared Error Loss: {loss.item()}")