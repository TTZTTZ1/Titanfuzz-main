import torch
import torch.nn.functional as F

# Create random input and target tensors
input_tensor = torch.randn(3, requires_grad=True)
target_tensor = torch.randn(3)

# Compute MSE loss with reduction='sum'
loss = F.mse_loss(input_tensor, target_tensor, reduction='sum')

# Print the computed loss
print("Computed MSE Loss:", loss.item())

# Backward pass to compute gradients
loss.backward()
print("Gradients of input tensor:", input_tensor.grad)