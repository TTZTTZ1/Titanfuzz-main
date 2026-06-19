import torch
from torch.nn.functional import mse_loss

# Create some example tensors
input_tensor = torch.randn(3, requires_grad=True)
target_tensor = torch.tensor([1.0, 2.0, 3.0])

# Compute the MSE loss
loss = mse_loss(input_tensor, target_tensor, reduction='mean')

# Print the loss
print(loss)

# Backward pass
loss.backward()