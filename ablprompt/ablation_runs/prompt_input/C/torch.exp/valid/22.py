import torch

# Create a random tensor with float32 data type
input_tensor = torch.randn(3, 3, dtype=torch.float32)

# Compute the exponential of each element in the tensor
output_tensor = torch.exp(input_tensor)

print(output_tensor)