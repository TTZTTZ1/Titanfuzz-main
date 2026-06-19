import torch
import torch.nn.functional as F

# Example tensors for demonstration
input_tensor = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
target_tensor = torch.tensor([1.5, 2.5, 3.5])

# Calculate Mean Squared Error Loss
loss = F.mse_loss(input_tensor, target_tensor)

print(f"Mean Squared Error Loss: {loss.item()}")