import torch
from torch.nn.functional import mse_loss

# Example tensors
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
target_tensor = torch.tensor([[1.5, 2.5], [3.5, 4.5]])

# Compute MSE loss with reduction='sum'
loss = mse_loss(input_tensor, target_tensor, reduction='sum')

print(f"MSE Loss: {loss.item()}")