import torch

# Create a random tensor with values between -π and π
input_tensor = torch.rand(5) * 2 * torch.pi - torch.pi

# Compute the cosine of each element in the input tensor
cosine_values = torch.cos(input_tensor)

print("Input Tensor:", input_tensor)
print("Cosine Values:", cosine_values)