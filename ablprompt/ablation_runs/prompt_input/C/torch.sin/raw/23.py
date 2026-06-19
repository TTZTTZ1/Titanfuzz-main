import torch

# Create a random tensor with complex numbers
input_tensor = torch.randn(3, 3) + 1j * torch.randn(3, 3)

# Compute the sine of each element in the input tensor
output_tensor = torch.sin(input_tensor)

print("Input Tensor:\n", input_tensor)
print("Output Tensor (Sine):\n", output_tensor)