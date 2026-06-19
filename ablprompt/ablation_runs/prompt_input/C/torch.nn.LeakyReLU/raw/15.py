import torch
import torch.nn as nn

# Create a LeakyReLU layer with a custom negative slope
leaky_relu = nn.LeakyReLU(negative_slope=0.1)

# Generate a random input tensor
input_tensor = torch.randn(3, 4, requires_grad=True)

# Apply the LeakyReLU activation
output_tensor = leaky_relu(input_tensor)

# Compute the loss (example: mean squared error)
target_tensor = torch.randn(3, 4)
loss_fn = nn.MSELoss()
loss = loss_fn(output_tensor, target_tensor)

# Backward pass to compute gradients
loss.backward()

# Print the output and gradients
print("Output Tensor:", output_tensor)
print("Gradients:", input_tensor.grad)