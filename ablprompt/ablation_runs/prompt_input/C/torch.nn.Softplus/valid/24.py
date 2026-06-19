import torch

# Create a Softplus layer with custom beta and threshold
softplus = torch.nn.Softplus(beta=2.0, threshold=30.0)

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0, 2.0])

# Apply Softplus activation
output_tensor = softplus(input_tensor)

print(output_tensor)