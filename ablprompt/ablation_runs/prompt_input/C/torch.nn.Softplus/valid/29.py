import torch

# Create an instance of Softplus with custom beta and threshold
softplus = torch.nn.Softplus(beta=0.5, threshold=10.0)

# Generate a random input tensor
input_tensor = torch.randn(3, 3)

# Apply the Softplus activation function
output_tensor = softplus(input_tensor)

print(output_tensor)