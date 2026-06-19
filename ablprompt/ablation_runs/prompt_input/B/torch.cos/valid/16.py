import torch

# Create a random tensor with values between -pi and pi
input_tensor = torch.rand(5) * 2 * torch.pi - torch.pi

# Compute the cosine of the input tensor
output_tensor = torch.cos(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)