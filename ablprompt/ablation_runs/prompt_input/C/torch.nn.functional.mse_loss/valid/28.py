import torch
import torch.nn.functional as F

# Generate random input and target tensors
input_tensor = torch.randn(3, requires_grad=True)
target_tensor = torch.randn(3)

# Compute MSE loss with reduction='mean'
mse_loss = F.mse_loss(input_tensor, target_tensor, reduction='mean')

# Print the computed loss
print("MSE Loss:", mse_loss.item())

# Backward pass to compute gradients
mse_loss.backward()
print("Gradients of input tensor:", input_tensor.grad)