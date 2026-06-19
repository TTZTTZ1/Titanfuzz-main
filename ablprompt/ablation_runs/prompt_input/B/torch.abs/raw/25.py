import torch

# Create a random tensor with both positive and negative values
input_tensor = torch.randn(5, 5)

# Compute the absolute value of the tensor
abs_tensor = torch.abs(input_tensor)

print("Input Tensor:", input_tensor)
print("Absolute Value Tensor:", abs_tensor)