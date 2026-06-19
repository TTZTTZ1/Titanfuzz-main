import torch
from torch.nn import functional as F

# Example tensors
input_tensor = torch.randn(3, requires_grad=True)
target_tensor = torch.tensor([1.0, 2.0, 3.0])

# Compute MSE loss with custom reduction and weighting
weight = torch.tensor([0.5, 1.0, 1.5])
mse_loss = F.mse_loss(input_tensor, target_tensor, reduction='none', weight=weight)

print("MSE Loss:", mse_loss)