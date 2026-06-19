import torch
import torch.nn.functional as F

# Create some random tensors for demonstration
input_tensor = torch.randn(3, requires_grad=True)
target_tensor = torch.randn(3)

# Calculate Mean Squared Error loss
loss = F.mse_loss(input_tensor, target_tensor)

print(f"Loss: {loss.item()}")