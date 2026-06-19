import torch
import torch.nn as nn

# Create a Softplus layer with custom beta and threshold
softplus_layer = nn.Softplus(beta=0.5, threshold=10.0)

# Define a random input tensor
input_tensor = torch.randn(3, 4, requires_grad=True)

# Apply the Softplus activation
output_tensor = softplus_layer(input_tensor)

# Print the input and output tensors
print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)

# Compute gradients
loss = output_tensor.sum()
loss.backward()

# Print gradients
print("Gradients of Input Tensor:", input_tensor.grad)