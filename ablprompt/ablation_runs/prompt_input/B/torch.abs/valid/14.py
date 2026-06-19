import torch

# Create a random tensor with both positive and negative values
input_tensor = torch.tensor([-3.5, 0, 2.5, -1.0], dtype=torch.float)

# Compute the element-wise absolute value
abs_tensor = torch.abs(input_tensor)

print("Input Tensor:", input_tensor)
print("Absolute Value Tensor:", abs_tensor)