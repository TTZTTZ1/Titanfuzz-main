import torch

# Create a random tensor with negative and positive values
input_tensor = torch.randn(5, 5) * 10  # Scale by 10 to ensure some negative values

# Compute the element-wise square root
output_tensor = torch.sqrt(input_tensor)

print("Input Tensor:\n", input_tensor)
print("Output Tensor:\n", output_tensor)