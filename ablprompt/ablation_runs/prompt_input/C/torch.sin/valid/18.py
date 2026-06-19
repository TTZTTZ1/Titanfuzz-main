import torch

# Create a tensor with random values between -π and π
input_tensor = torch.rand(5) * 2 * torch.pi - torch.pi

# Compute the sine of each element in the tensor
output_tensor = torch.sin(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor (Sine Values):", output_tensor)