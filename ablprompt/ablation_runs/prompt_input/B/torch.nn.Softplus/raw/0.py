import torch

# Create a tensor with random values
input_tensor = torch.randn(5, 5)

# Initialize Softplus with custom beta and threshold
softplus = torch.nn.Softplus(beta=0.5, threshold=10.0)

# Apply Softplus activation
output_tensor = softplus(input_tensor)

print(output_tensor)