import torch

# Create a random tensor with both positive and negative values
input_tensor = torch.tensor([-3, -1, 0, 2, 4], dtype=torch.float)

# Compute the absolute value of the tensor
abs_tensor = torch.abs(input_tensor)

print("Input Tensor:", input_tensor)
print("Absolute Value Tensor:", abs_tensor)