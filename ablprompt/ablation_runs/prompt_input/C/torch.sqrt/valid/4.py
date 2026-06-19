import torch

# Create a random tensor with positive values
input_tensor = torch.rand(5, 5)

# Compute the square root of the input tensor
output_tensor = torch.sqrt(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("\nSquare Root Output Tensor:")
print(output_tensor)