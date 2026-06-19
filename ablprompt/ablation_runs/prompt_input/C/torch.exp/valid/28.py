import torch

# Create a random input tensor with float32 data type
input_tensor = torch.randn(3, 3, dtype=torch.float32)

# Compute the exponential of the input tensor
output_tensor = torch.exp(input_tensor)

print(output_tensor)