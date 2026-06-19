import torch
import torch.nn.functional as F

# Example tensors
input = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
target = torch.tensor([[1.5, 2.5], [3.5, 4.5]])

# Calculate Mean Squared Error Loss
loss = F.mse_loss(input, target)

print(f"Mean Squared Error Loss: {loss.item()}")