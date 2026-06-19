import torch

# Create a random complex tensor
input_tensor = torch.randn(3, 4) + 1j * torch.randn(3, 4)

# Compute the absolute value using torch.abs
output_tensor = torch.abs(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)