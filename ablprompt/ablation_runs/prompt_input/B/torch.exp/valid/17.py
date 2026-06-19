import torch

# Create a random tensor with float32 data type
input_tensor = torch.randn(5, 5, dtype=torch.float32)

# Compute the exponential of each element in the input tensor
output_tensor = torch.exp(input_tensor)

print(output_tensor)