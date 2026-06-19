import torch
import torch.nn.functional as F

# Create some random tensors for demonstration
input_tensor = torch.randn(3, 5)
target_tensor = torch.randn(3, 5)

# Calculate Mean Squared Error loss
loss = F.mse_loss(input_tensor, target_tensor)

print(f"Mean Squared Error Loss: {loss.item()}")