import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(3, 4, requires_grad=True)

# Define LeakyReLU with a custom slope
leaky_relu = nn.LeakyReLU(negative_slope=0.1)

# Apply LeakyReLU to the input tensor
output_tensor = leaky_relu(input_tensor)

# Perform some operations to require gradient computation
loss = output_tensor.sum()

# Compute gradients
loss.backward()