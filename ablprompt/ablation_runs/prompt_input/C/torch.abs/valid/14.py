import torch

# Create a tensor with both positive and negative values
input_tensor = torch.tensor([-1.5, 0.0, 2.3, -4.7], dtype=torch.float)

# Compute the absolute value of the tensor
abs_tensor = torch.abs(input_tensor)

print("Input Tensor:", input_tensor)
print("Absolute Value Tensor:", abs_tensor)