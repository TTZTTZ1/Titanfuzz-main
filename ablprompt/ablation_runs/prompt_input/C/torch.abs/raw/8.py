import torch

# Create a tensor with both positive and negative values
input_tensor = torch.tensor([-3, -2, 0, 2, 3], dtype=torch.float)

# Compute the absolute values
abs_tensor = torch.abs(input_tensor)

print("Input Tensor:", input_tensor)
print("Absolute Values:", abs_tensor)