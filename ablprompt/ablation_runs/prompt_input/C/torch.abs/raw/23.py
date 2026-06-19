import torch

# Create a tensor with both positive and negative values
input_tensor = torch.tensor([-1, -2, 3, 4], dtype=torch.float)

# Compute the absolute value using torch.abs
abs_tensor = torch.abs(input_tensor)

print("Input Tensor:", input_tensor)
print("Absolute Value Tensor:", abs_tensor)