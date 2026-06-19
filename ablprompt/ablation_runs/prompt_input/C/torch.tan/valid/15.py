import torch

# Create a tensor with random float values between -π/2 and π/2
input_tensor = torch.rand(5) * torch.pi / 2 - torch.pi / 4

# Compute the tangent of each element in the input tensor
output_tensor = torch.tan(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)