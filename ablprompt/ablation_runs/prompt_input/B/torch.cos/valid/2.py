import torch

# Create a random tensor with float32 data type
input_tensor = torch.randn(3, 4, dtype=torch.float32)

# Compute the cosine of each element in the input tensor
output_tensor = torch.cos(input_tensor)

print(output_tensor)