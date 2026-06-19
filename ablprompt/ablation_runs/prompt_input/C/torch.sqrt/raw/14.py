import torch

# Create a random tensor with float32 data type
input_tensor = torch.randn(5, 5, dtype=torch.float32)

# Compute the square root using torch.sqrt
output_tensor = torch.sqrt(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)