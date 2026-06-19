import torch

# Create a random complex tensor
input_tensor = torch.randn(3, 4) + 1j * torch.randn(3, 4)

# Compute the element-wise absolute value
abs_tensor = torch.abs(input_tensor)

print(abs_tensor)