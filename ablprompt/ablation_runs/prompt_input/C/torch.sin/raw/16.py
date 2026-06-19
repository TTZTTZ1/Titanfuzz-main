import torch

# Create a tensor with random float values between 0 and 2*pi
input_tensor = torch.rand(5) * (2 * torch.pi)

# Compute the sine of each element in the input tensor
output_tensor = torch.sin(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)