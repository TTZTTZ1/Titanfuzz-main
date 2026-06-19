import torch

# Create a random tensor with positive values
input_tensor = torch.rand(5, 5) * 10  # Ensure values are non-negative

# Compute the square root using torch.sqrt
output_tensor = torch.sqrt(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("Output Tensor (Square Roots):")
print(output_tensor)