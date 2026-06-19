import torch

# Create a Softplus layer with custom beta and threshold
softplus = torch.nn.Softplus(beta=2.0, threshold=30.0)

# Define an input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0], requires_grad=True)

# Apply the Softplus activation
output = softplus(input_tensor)

# Compute the gradient
output.sum().backward()

print("Output:", output)
print("Gradient:", input_tensor.grad)