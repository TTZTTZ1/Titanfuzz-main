import torch

# Create a random tensor of floats
input_tensor = torch.randn(5, 5, requires_grad=True)

# Compute the exponential of each element in the tensor
output_tensor = torch.exp(input_tensor)

# Print the result
print(output_tensor)