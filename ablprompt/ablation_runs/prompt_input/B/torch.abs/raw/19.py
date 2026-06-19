import torch

# Create a random tensor with both positive and negative values
input_tensor = torch.tensor([-3.5, -1.0, 0.0, 2.0, 4.5], dtype=torch.float32)

# Compute the absolute value using torch.abs
abs_tensor = torch.abs(input_tensor)

print("Input Tensor:", input_tensor)
print("Absolute Value Tensor:", abs_tensor)