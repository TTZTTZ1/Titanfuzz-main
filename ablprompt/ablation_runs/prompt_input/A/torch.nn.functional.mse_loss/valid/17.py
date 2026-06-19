import torch
import torch.nn.functional as F

# Example tensors
input = torch.tensor([0.5, 1.5], requires_grad=True)
target = torch.tensor([1.0, 2.0])

# Compute Mean Squared Error loss
loss = F.mse_loss(input, target)

print(f"Loss: {loss.item()}")