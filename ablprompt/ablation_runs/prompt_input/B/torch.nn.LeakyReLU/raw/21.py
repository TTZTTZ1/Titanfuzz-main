import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(3, 4, requires_grad=True)

# Define LeakyReLU with a custom negative slope
leaky_relu = nn.LeakyReLU(negative_slope=0.1)

# Apply LeakyReLU to the input tensor
output_tensor = leaky_relu(input_tensor)

# Compute the loss (example: mean squared error)
target_tensor = torch.randn_like(output_tensor)
loss_fn = nn.MSELoss()
loss = loss_fn(output_tensor, target_tensor)

# Backward pass
loss.backward()

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)
print("Loss:", loss)