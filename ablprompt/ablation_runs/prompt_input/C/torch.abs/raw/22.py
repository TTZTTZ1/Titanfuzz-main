import torch

# Create a random complex tensor
input_tensor = torch.randn(3, 4) + 1j * torch.randn(3, 4)

# Compute the absolute value using torch.abs
abs_tensor = torch.abs(input_tensor)

print("Input Tensor:", input_tensor)
print("Absolute Value Tensor:", abs_tensor)