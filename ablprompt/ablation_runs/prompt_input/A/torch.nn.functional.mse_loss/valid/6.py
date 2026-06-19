import torch
import torch.nn.functional as F

# Create some sample tensors
input_tensor = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
target_tensor = torch.tensor([1.5, 2.5, 3.5])

# Calculate Mean Squared Error Loss
loss = F.mse_loss(input_tensor, target_tensor)

print(f"Mean Squared Error Loss: {loss.item()}")

# Backward pass to compute gradients
loss.backward()
print(f"Gradient of input tensor: {input_tensor.grad}")