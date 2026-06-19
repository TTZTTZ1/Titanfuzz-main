import torch

# Create a random tensor with float32 data type
input_tensor = torch.randn(3, 3, dtype=torch.float32)

# Compute the tangent of each element in the tensor
output_tensor = torch.tan(input_tensor)

print("Input Tensor:\n", input_tensor)
print("Output Tensor:\n", output_tensor)