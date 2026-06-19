import torch

# Create a random tensor with both positive and negative values
input_tensor = torch.randn(3, 4)

# Compute the absolute value of the tensor
abs_tensor = torch.abs(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("\nAbsolute Value Tensor:")
print(abs_tensor)