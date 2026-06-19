import torch

# Create a random tensor of floats
input_tensor = torch.randn(5, 5, dtype=torch.float32)

# Compute the exponential of each element in the tensor
output_tensor = torch.exp(input_tensor)

print(output_tensor)