import torch

# Create a tensor with random values in radians
input_tensor = torch.randn(4, 4)

# Compute the tangent of each element in the tensor
output_tensor = torch.tan(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("Output Tensor:")
print(output_tensor)