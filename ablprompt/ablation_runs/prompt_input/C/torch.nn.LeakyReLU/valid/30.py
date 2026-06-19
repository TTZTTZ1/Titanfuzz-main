import torch
import torch.nn as nn

# Create a LeakyReLU layer with a custom slope
leaky_relu = nn.LeakyReLU(negative_slope=0.1)

# Define an input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0], requires_grad=True)

# Apply the LeakyReLU activation
output = leaky_relu(input_tensor)

# Compute the loss
loss = output.sum()

# Backward pass
loss.backward()

print("Output:", output)
print("Gradient:", input_tensor.grad)