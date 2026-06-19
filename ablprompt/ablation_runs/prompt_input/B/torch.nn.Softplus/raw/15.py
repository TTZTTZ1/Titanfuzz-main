import torch

# Create a tensor with random values
input_tensor = torch.randn(3, 4)

# Initialize the Softplus layer with custom beta and threshold
softplus = torch.nn.Softplus(beta=0.5, threshold=10.0)

# Apply the Softplus activation function
output_tensor = softplus(input_tensor)

print(output_tensor)