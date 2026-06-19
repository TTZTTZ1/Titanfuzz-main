import torch

# Create a tensor with random values in radians
input_tensor = torch.rand(5) * torch.pi

# Compute the tangent of each element in the tensor
output_tensor = torch.tan(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)