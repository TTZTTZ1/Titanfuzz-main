import torch

# Create a random tensor with values between -5 and 10
input_tensor = torch.rand(3, 4) * 15 - 5

# Clamp the tensor to the range [-2, 8]
clamped_tensor = torch.clamp(input_tensor, min=-2, max=8)

print("Original Tensor:", input_tensor)
print("Clamped Tensor:", clamped_tensor)