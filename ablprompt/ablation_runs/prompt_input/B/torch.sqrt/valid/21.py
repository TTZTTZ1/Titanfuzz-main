import torch

# Create a random tensor with negative and positive values
input_tensor = torch.randn(5) * 10

# Compute the square root of the tensor
output_tensor = torch.sqrt(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)