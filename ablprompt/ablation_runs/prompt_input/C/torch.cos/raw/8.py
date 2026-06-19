import torch

# Create a tensor with random values between 0 and 2*pi
input_tensor = torch.rand(5) * 2 * torch.pi

# Compute the cosine of each element in the input tensor
cosine_values = torch.cos(input_tensor)

print("Input Tensor:", input_tensor)
print("Cosine Values:", cosine_values)