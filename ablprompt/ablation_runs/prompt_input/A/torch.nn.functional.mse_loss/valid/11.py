import torch
import torch.nn.functional as F

# Example tensors
input = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
target = torch.tensor([1.5, 2.5, 3.5])

# Calculate Mean Squared Error loss
loss = F.mse_loss(input, target)

print(f"Calculated Loss: {loss.item()}")