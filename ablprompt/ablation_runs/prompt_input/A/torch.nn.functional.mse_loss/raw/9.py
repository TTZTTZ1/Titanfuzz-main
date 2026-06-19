import torch
import torch.nn.functional as F

# Create some sample tensors
input_tensor = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
target_tensor = torch.tensor([1.5, 2.5, 3.5])

# Compute the MSE loss
mse_loss = F.mse_loss(input_tensor, target_tensor)

print(f"MSE Loss: {mse_loss.item()}")