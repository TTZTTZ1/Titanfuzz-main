import torch

# Create an instance of Softplus with custom beta and threshold
softplus = torch.nn.Softplus(beta=0.5, threshold=15.0)

# Generate a random input tensor
input_tensor = torch.randn(3, 4, requires_grad=True)

# Apply Softplus activation
output_tensor = softplus(input_tensor)

# Compute the gradient
loss = output_tensor.sum()
loss.backward()

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)
print("Gradient of Input Tensor:", input_tensor.grad)