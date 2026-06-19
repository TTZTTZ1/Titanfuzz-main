import torch

# Create a Softplus layer with custom beta and threshold
softplus = torch.nn.Softplus(beta=0.5, threshold=10.0)

# Define an input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0], requires_grad=True)

# Apply the Softplus function
output_tensor = softplus(input_tensor)

# Compute the gradient
output_tensor.sum().backward()

print("Output:", output_tensor)
print("Gradient:", input_tensor.grad)