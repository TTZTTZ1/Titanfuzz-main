import torch
import torch.nn as nn

# Create a LeakyReLU layer with a custom negative slope
leaky_relu = nn.LeakyReLU(negative_slope=0.1)

# Create an input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0], requires_grad=True)

# Apply the LeakyReLU activation
output_tensor = leaky_relu(input_tensor)

# Compute the loss (example: mean squared error)
target_tensor = torch.tensor([0.0, 0.0, 1.0])
loss = ((output_tensor - target_tensor) ** 2).mean()

# Backward pass to compute gradients
loss.backward()

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)
print("Gradients:", input_tensor.grad)