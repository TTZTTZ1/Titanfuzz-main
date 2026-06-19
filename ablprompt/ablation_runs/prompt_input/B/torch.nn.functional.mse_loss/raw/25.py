import torch
from torch.nn.functional import mse_loss

# Create some random tensors for input and target
input_tensor = torch.randn(3, 5)
target_tensor = torch.randn(3, 5)

# Calculate the MSE loss with 'mean' reduction
loss = mse_loss(input_tensor, target_tensor, reduction='mean')

print(loss)