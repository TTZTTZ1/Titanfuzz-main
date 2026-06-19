import torch

# Create a random tensor with float32 data type
input_tensor = torch.randn(3, 3, dtype=torch.float32)

# Compute the tangent of each element in the input tensor
output_tensor = torch.tan(input_tensor)

print(output_tensor)