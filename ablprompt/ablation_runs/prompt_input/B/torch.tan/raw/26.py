import torch

# Create an input tensor with random values between -π/2 and π/2
input_tensor = torch.rand(10) * torch.pi / 2 - torch.pi / 4

# Compute the tangent of the input tensor
output_tensor = torch.tan(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)