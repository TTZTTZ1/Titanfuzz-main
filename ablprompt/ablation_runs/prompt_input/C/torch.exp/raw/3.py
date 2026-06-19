import torch

# Create a random input tensor
input_tensor = torch.randn(3, 3, requires_grad=True)

# Compute the exponential of the input tensor
output_tensor = torch.exp(input_tensor)

# Print the result
print(output_tensor)