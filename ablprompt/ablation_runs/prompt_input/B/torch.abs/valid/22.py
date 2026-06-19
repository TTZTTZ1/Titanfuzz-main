import torch

# Create a random tensor with both positive and negative values
input_tensor = torch.randn(5, 5)

# Compute the absolute value using torch.abs
output_tensor = torch.abs(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("\nOutput Tensor after applying torch.abs:")
print(output_tensor)