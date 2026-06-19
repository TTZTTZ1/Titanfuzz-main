import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(3, 4, requires_grad=True)

# Define the GELU layer with the 'tanh' approximation
gelu_layer = nn.GELU(approximate='tanh')

# Apply the GELU layer to the input tensor
output_tensor = gelu_layer(input_tensor)

# Compute the loss
loss = output_tensor.sum()

# Backward pass to compute gradients
loss.backward()

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)
print("Gradients:", input_tensor.grad)