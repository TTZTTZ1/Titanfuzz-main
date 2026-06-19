import torch

# Create a complex tensor with random values in radians
input_tensor = torch.randn(5, dtype=torch.float32) * 2 * torch.pi

# Compute the cosine of each element
output_tensor = torch.cos(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)