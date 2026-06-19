import torch

# Create a random tensor with both positive and negative values
input_tensor = torch.randn(3, 4) * 10  # Multiplying by 10 to ensure some negative values

# Compute the absolute value using torch.abs
abs_tensor = torch.abs(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("\nAbsolute Value Tensor:")
print(abs_tensor)