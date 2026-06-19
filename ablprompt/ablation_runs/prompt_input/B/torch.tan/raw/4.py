import torch

# Create a random tensor with float32 data type
input_tensor = torch.randn(3, 3, requires_grad=True)

# Compute the tangent of the input tensor
output_tensor = torch.tan(input_tensor)

# Print the result
print(output_tensor)