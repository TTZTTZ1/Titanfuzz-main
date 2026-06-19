import torch

# Create a complex tensor
input_tensor = torch.tensor([-1 + 2j, -3 - 4j, 5 + 6j])

# Compute the absolute values using torch.abs
abs_tensor = torch.abs(input_tensor)

print("Input Tensor:", input_tensor)
print("Absolute Values:", abs_tensor)