import torch
import torch.nn.functional as F

# Create some dummy tensors for input and target
input_tensor = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
target_tensor = torch.tensor([1.5, 2.5, 3.5])

# Calculate Mean Squared Error loss
loss = F.mse_loss(input_tensor, target_tensor)

print(f"Calculated Loss: {loss.item()}")