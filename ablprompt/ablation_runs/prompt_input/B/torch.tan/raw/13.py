import torch

# Create a random tensor with float32 dtype
input_tensor = torch.randn(4, 4, dtype=torch.float32)

# Compute the tangent of each element in the input tensor
output_tensor = torch.tan(input_tensor)

print(output_tensor)