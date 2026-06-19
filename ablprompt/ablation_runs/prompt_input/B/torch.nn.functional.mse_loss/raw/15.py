import torch
from torch.nn.functional import mse_loss

# Example usage of mse_loss with weighting and reduction
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
target_tensor = torch.tensor([[1.5, 2.5], [3.5, 4.5]])
weight_tensor = torch.tensor([0.5, 1.0])

loss = mse_loss(input_tensor, target_tensor, weight=weight_tensor, reduction='mean')
print(loss)