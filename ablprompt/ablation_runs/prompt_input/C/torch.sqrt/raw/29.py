import torch

# Create a random tensor with positive values
input_tensor = torch.rand(5, 5) * 10  # Multiplying by 10 ensures all elements are positive

# Compute the square root of the input tensor
output_tensor = torch.sqrt(input_tensor)

print("Input Tensor:\n", input_tensor)
print("Output Tensor (Square Root):\n", output_tensor)