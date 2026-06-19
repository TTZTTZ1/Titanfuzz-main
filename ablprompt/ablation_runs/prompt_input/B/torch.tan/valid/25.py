import torch

# Create a random tensor with values in radians
input_tensor = torch.rand(5) * (2 * torch.pi) - torch.pi

# Compute the tangent of each element in the input tensor
output_tensor = torch.tan(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)