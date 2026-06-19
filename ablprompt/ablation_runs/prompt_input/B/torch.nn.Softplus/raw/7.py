import torch

# Create a tensor with random values
input_tensor = torch.randn(3, 4, requires_grad=True)

# Initialize the Softplus layer with custom beta and threshold
softplus_layer = torch.nn.Softplus(beta=2.0, threshold=15.0)

# Apply the Softplus layer to the input tensor
output_tensor = softplus_layer(input_tensor)

# Compute the gradient
output_tensor.sum().backward()

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)
print("Gradient of Input Tensor:", input_tensor.grad)