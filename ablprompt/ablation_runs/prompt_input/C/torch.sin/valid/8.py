import torch

# Create a tensor with random values between -π/2 and π/2
input_tensor = torch.rand(5) * torch.pi / 2 - torch.pi / 2

# Compute the sine of each element in the tensor
output_tensor = torch.sin(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor (Sine):", output_tensor)