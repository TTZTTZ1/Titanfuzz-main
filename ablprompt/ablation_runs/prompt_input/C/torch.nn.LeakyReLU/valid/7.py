import torch
import torch.nn as nn

# Create a LeakyReLU layer with a custom slope
leaky_relu = nn.LeakyReLU(negative_slope=0.1)

# Create a random input tensor
input_tensor = torch.randn(3, 5, requires_grad=True)

# Apply the LeakyReLU activation
output_tensor = leaky_relu(input_tensor)

# Compute the loss (example: mean squared error)
target_tensor = torch.randn_like(output_tensor)
loss = ((output_tensor - target_tensor) ** 2).mean()

# Backward pass to compute gradients
loss.backward()